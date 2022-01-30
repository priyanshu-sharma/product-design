from django_filters import rest_framework as filters
from product_domain.models import HandbagDetail
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class HandbagDetailFilter(filters.FilterSet):
    product_id = filters.NumberFilter(field_name='product__id', lookup_expr='exact')
    product_id__in = NumberInFilter(field_name='product__id', lookup_expr='in')
    product_id__gte = NumberInFilter(field_name='product__id', lookup_expr='gte')
    product_id__lte = NumberInFilter(field_name='product__id', lookup_expr='lte')
    product_type = filters.CharFilter(field_name='product__type', lookup_expr='exact')
    product_type__in = CharInFilter(field_name='product__type', lookup_expr='in')
    product_name = filters.CharFilter(field_name='product__name', lookup_expr='exact')
    product_name__in = CharInFilter(field_name='product__name', lookup_expr='in')
    strict = True

    class Meta:
        model = HandbagDetail
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'name': ['exact', 'in'],
            'type': ['exact', 'in'],
        }
