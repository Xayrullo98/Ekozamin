from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func

from db import Base

class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer,ForeignKey('Customers.id'), nullable=False)
    comment = Column(String(200),nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id',), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)