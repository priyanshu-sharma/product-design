from django.db import models
from product_domain.enums import AccessoriesType
from product_domain.models.product_detail import ProductDetail
from extensions.exceptions.common_exceptions import ResourceNotFoundException


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

    @staticmethod
    def create(name, url, description, meta, product):
        """
        Create a product detail.
        """
        handbag_detail = HandbagDetail.objects.create(
            name=name, url=url, description=description, meta=meta, product=product
        )
        return handbag_detail

    @staticmethod
    def get_handbag_details(id):
        """
        Get handbag details based on id.
        """
        try:
            handbag_detail = HandbagDetail.objects.get(id=id)
            return handbag_detail
        except HandbagDetail.DoesNotExist:
            raise ResourceNotFoundException()
    
    @staticmethod
    def disable_older_handbag_details():
        """
        Disable older handbag details.
        """
        return HandbagDetail.objects.filter(active=False).update(active=False)
