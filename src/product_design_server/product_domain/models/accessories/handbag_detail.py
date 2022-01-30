from django.db import models
from product_domain.enums import AccessoriesType
from product_domain.models.product_detail import ProductDetail


class HandbagDetail(ProductDetail):
    """
    HandbagDetail model
    """
    type = models.TextField(default=AccessoriesType.HANDBAGS)

    class Meta:
        db_table = 'pd_handbag_detail'
        unique_together = [('name', 'type')]
        app_label = 'product_domain'
        indexes = [
            models.Index(fields=['name', 'type']),
        ]