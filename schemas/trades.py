from typing import Union

from pydantic import BaseModel
from typing import Optional


class TradeBase(BaseModel):
    product_id: int
    quantity: float
    price: int


class TradeCreate(TradeBase):
    user_id: int
    order_id: int


class TradeOut(TradeBase):
    id: int
