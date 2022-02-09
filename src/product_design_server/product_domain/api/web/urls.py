from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product_domain.api.web.views import HandbagDetailViewSet

router = DefaultRouter()
router.register(
    r"handbag_detail", HandbagDetailViewSet, basename="handbag_detail",
)

urlpatterns = [
    path("", include(router.urls)),
]
