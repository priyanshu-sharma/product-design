from sqlalchemy import Column, Integer


class UserTrackingModel(object):
    created_by_id = Column(Integer, nullable=True)
    updated_by_id = Column(Integer, nullable=True)
