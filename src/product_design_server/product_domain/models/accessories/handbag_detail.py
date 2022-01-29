from django.db import models
from product_domain.enums import ProductType
from product_domain.models.product_detail import ProductDetail


class HandbagDetail(ProductDetail):
    """
    HandbagDetail model
    """
    product_type = models.TextField(default=ProductType.ACCESSORIES)

    class Meta:
        db_table = 'pd_handbag_detail'
        unique_together = [('name', 'product_type')]
        app_label = 'product_domain'
        indexes = [
            models.Index(fields=['name', 'product_type']),
        ]