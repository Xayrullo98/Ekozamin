from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.orm import relationship

from db import Base

class Customers(Base):
    __tablename__ = "Customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    comment = Column(String(200),nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id',), nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    