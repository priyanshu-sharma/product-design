from extensions.utils import Singleton
from services.product_design_service import ProductDesignService

class ServiceRegistry(metaclass=Singleton):
    def __init__(self):
        pass

    @property
    def product_design_client(self):
        host = product_design_config["host"]
        user = product_design_config["user"]
        password = product_design_config["password"]
        return ProductDesignService(host, user, password)

registry = ServiceRegistry()
