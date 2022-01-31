from datetime import datetime
from sqlalchemy import Column, DateTime, func


class AutoTimestampedModel(object):
    install_ts = Column(DateTime(timezone=True), server_default=func.now())
    update_ts = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
