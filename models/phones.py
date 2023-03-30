from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func, and_
from sqlalchemy.orm import relationship, backref
from db import Base
from .customers import Customers
from .users import Users


class Phones(Base):
    __tablename__ = "Phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(20), nullable=False)
    source_id = Column(Integer, nullable=False)
    source = Column(String(20),nullable=True)
    comment = Column(String(200),nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    for_user = relationship('Users', foreign_keys=[source_id], backref=backref('number', order_by="desc(Phones.id)"), primaryjoin=lambda: and_(Users.id == Phones.source_id, Phones.source == "for_user"))
    for_customer = relationship('Customers', foreign_keys=[source_id], backref=backref('number', order_by="desc(Phones.id)"), primaryjoin=lambda: and_(Customers.id == Phones.source_id, Phones.source == "for_customer"))

    user = relationship('Users',back_populates='auth')