from rest_framework import serializers
from product_domain.enums import AccessoriesType

class HandbagCreationSerializer(serializers.Serializer):
    name = serializers.CharField()
    type = serializers.ChoiceField(choices=AccessoriesType.choices(), default=AccessoriesType.HANDBAGS)
    url = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, allow_null=True, default=None)
    metadata = serializers.JSONField(default=dict)