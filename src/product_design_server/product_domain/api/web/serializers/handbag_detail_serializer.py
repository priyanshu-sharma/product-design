from rest_framework import serializers

from product_domain.models import HandbagDetail


class HandbagDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_type = serializers.CharField(source='product.type')
    product_meta = serializers.JSONField(source='product.meta')
    product_description = serializers.CharField(source='product.description')

    class Meta:
        model = HandbagDetail
        fields = (
            'id',
            'install_ts',
            'update_ts',
            'created_by_id',
            'updated_by_id',
            'name',
            'type',
            'url',
            'description',
            'meta',
            'product_id',
            'product_type',
            'product_name',
            'product_meta',
            'product_description'
        )
