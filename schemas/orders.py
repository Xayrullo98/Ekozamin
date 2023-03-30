from pydantic import BaseModel
from typing import Optional


class OrderBase(BaseModel):
    customer_id: int
    comment: Optional[str]


class OrderCreate(OrderBase):
    user_id: int


class OrderOut(OrderBase):
    id: int
