from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from product_domain.enums import ProductType

class Product(AutoTimestampedModel, UserTrackingModel):
    """
    Product model.
    """
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.TextField(choices=ProductType.choices(), default=ProductType.CLOTHING)
    metadata = models.JSONField(default=dict)
    description = models.TextField()

    class Meta:
        db_table = 'pd_product'
        app_label = 'product_domain'
        unique_together = [('name', 'type')]
        indexes = [
            models.Index(fields=['name', 'type']),
        ]
