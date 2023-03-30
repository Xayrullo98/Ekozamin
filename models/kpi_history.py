from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func,Float

from db import Base

class Kpi_History(Base):
    __tablename__ = "Kpi_History"
    id = Column(Integer, primary_key=True)
    money = Column(Integer, nullable=True)
    trade_id = Column(Integer,ForeignKey('Trades.id'), nullable=False)
    comment = Column(String(200),nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id',), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)