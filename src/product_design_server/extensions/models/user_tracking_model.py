"""UserTrackingModel Abstract model

This model can be inherited to give created_by_id and updated_by_id
fields to your django model by default.
"""
from django.db import models


class UserTrackingModel(models.Model):
    """UserTrackingModel

    This model can be inherited to give created_by_id and updated_by_id
    fields to your django model by default.

    Extends:
        models.Model

    """

    created_by_id = models.IntegerField(null=True, blank=True)
    updated_by_id = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
