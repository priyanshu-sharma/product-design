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

class HandbagDetailViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = HandbagDetail.objects.select_related("product").all()
    serializer_class = HandbagDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = HandbagDetailFilter
    ordering_fields = ('id',)
    ordering = ('-id',)
    pagination_class = StandardPagination

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        product_creation_serializer = ProductCreationSerializer(data=request.data)
        product_creation_serializer.is_valid(raise_exception=True)
        serialized_data = product_creation_serializer.validated_data
        print(dict(serialized_data))
        return Response( 
            data ={
                "message": "Product and Product Detail created",
                "status": "Success"
            }, 
            status=status.HTTP_201_CREATED
        )
