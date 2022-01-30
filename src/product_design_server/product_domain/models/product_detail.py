from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from product_domain.enums import ProductType
from product_domain.models import Product

class ProductDetail(AutoTimestampedModel, UserTrackingModel):
    """
    ProductDetail model
    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=1000)
    description = models.TextField(null=True)
    metadata = models.JSONField(default=dict)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        app_label = 'product_domain'

    @staticmethod
    def get_or_create(name, url, description, metadata, product):
        raise NotImplementedError
