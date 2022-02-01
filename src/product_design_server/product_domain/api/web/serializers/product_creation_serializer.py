from rest_framework import serializers
from product_domain.enums import ProductType
from product_domain.api.web.serializers import HandbagCreationSerializer

class ProductCreationSerializer(serializers.Serializer):
    product_type = serializers.ChoiceField(choices=ProductType.choices())
    product_name = serializers.CharField()
    product_meta = serializers.JSONField(default=dict)
    product_description = serializers.CharField(max_length=255, allow_null=True, default=None)
    product_details = serializers.ListField(child=HandbagCreationSerializer(), allow_null=False, allow_empty=False)
