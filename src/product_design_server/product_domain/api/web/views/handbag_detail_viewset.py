from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter

from product_domain.api.web.filters import HandbagDetailFilter
from product_domain.api.web.serializers import HandbagDetailSerializer
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
