from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from product_domain.enums import ProductType

class Product(AutoTimestampedModel, UserTrackingModel):
    """
    Product model.
    """
    name = models.CharField(max_length=255)
    type = models.TextField(choices=ProductType.choices(), default=ProductType.CLOTHING)
    meta = models.JSONField(default=dict)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'pd_product'
        app_label = 'product_domain'
        unique_together = [('name', 'type')]
        indexes = [
            models.Index(fields=['name', 'type']),
        ]

    @staticmethod
    def get_or_create(name, type, meta, description):
        """
        Get or create a product.
        """
        try:
            product = Product.objects.get(name=name, type=type)
        except Product.DoesNotExist:
            product = Product.objects.create(name=name, type=type, meta=meta, description=description)
            product.save()
        return product