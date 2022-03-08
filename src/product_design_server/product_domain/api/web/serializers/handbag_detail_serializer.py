from rest_framework import serializers

from product_domain.models import HandbagDetail


class HandbagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbagDetail
        fields = (
            'id',
            'name',
            'type',
            'url',
            'description',
            'meta',
            'active',
            'product_id',
        )
