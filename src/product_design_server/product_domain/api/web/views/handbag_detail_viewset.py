from django_filters import rest_framework as filters

from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

from product_domain.api.web.filters import HandbagDetailFilter
from product_domain.api.web.serializers import HandbagDetailSerializer, ProductCreationSerializer
from product_domain.api.web.pagination import StandardPagination
from product_domain.models import HandbagDetail
from product_domain.tasks import product_creation_task, populate_redis_task


class HandbagDetailViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = HandbagDetail.objects.filter(active=True)
    serializer_class = HandbagDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = HandbagDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination

    def list(self, request, *args, **kwargs):
        from server_config import RedisClient
        import pickle
        redis_client = RedisClient().get_instance()
        handbag_detail_list = []
        image_keys_list = [key for key in redis_client.scan_iter("ip_*")]
        if len(image_keys_list) == 100:
            print("Fetching from Redis")
            for images_key in image_keys_list:
                pickled_handbag_detail = redis_client.get(images_key)
                handbag_detail = pickle.loads(pickled_handbag_detail)
                handbag_detail_list.append(handbag_detail)
        else:
            print("Fetching from Database")
            response = super().list(request, args, kwargs)
            handbag_details = dict(response.data).get("results", [])
            populate_redis_task.delay(handbag_details)
            handbag_detail_list = handbag_details
        return Response(handbag_detail_list, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def create(self, request):
        from product_domain.api.public import handbag_detail_api
        handbag_detail_api.disable_handbag_details()
        product_creation_serializer = ProductCreationSerializer(data=request.data)
        product_creation_serializer.is_valid(raise_exception=True)
        serialized_data = product_creation_serializer.validated_data
        transaction.on_commit(lambda: product_creation_task.delay(dict(serialized_data)))
        return Response(
            data={"message": "Product and Product Detail created", "status": "Success"}, status=status.HTTP_201_CREATED
        )
