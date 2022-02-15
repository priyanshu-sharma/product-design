from server_config.database import Base
from sqlalchemy import Column, JSON, String, Integer, ForeignKey, Enum
from extensions.models import AutoTimestampedModel, UserTrackingModel
from enums import AccessoriesType


class HandbagDetail(AutoTimestampedModel, UserTrackingModel, Base):
    __tablename__ = "pd_handbag_detail"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    url = Column(String(1000))
    description = Column(String(1000), nullable=True)
    meta = Column(JSON, default={})
    product_id = Column(Integer, ForeignKey("pd_product.id"))
    type = Column(Enum(AccessoriesType), default=AccessoriesType.HANDBAGS)
