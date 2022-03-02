from extensions.utils import Singleton
from services.product_design_service import ProductDesignService
from server_config import product_design_config

class ServiceRegistry(metaclass=Singleton):
    def __init__(self):
        pass

    @property
    def product_design_client(self):
        host = product_design_config["host"]
        return ProductDesignService(host)

registry = ServiceRegistry()
