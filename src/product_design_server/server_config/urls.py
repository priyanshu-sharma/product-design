"""product_design_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from server_config import health_check_view
from product_domain.api.web import urls as product_domain_urls

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Product Design Server API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url("^health_check$", health_check_view),
    url('^docs/', schema_view),
    url("^api/product_domain/v1/", include((product_domain_urls, 'product_domain'), namespace='v1_product_domain')),
]
