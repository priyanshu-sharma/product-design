from server_config.database import Base
from sqlalchemy import Column, JSON, String, Integer, Enum
from extensions.models import AutoTimestampedModel, UserTrackingModel
from enums import ProductType

class Product(AutoTimestampedModel, UserTrackingModel, Base):
    __tablename__ = "pd_product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    type = Column(Enum(ProductType), default=ProductType.CLOTHING)
    meta = Column(JSON, default={})
    description = Column(String(1000), nullable=True)
