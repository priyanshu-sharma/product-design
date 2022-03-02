import logging

from server_config import settings
from services.base_service import BaseService

logger = logging.getLogger(__name__)


class ProductDesignService(BaseService):
    def __init__(self, host=None):
        super(ProductDesignService, self).__init__(host, None)

    def create_handbag_details(self, data):
        endpoint = "/api/product_domain/v1/handbag_detail/"
        response = self.post(endpoint, data=data)
        return response
