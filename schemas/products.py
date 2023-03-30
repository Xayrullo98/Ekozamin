from typing import Union

from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    birlik:str
    comment: Optional[str]
    price: int


class ProductCreate(ProductBase):
    user_id: int


class ProductOut(ProductBase):
    id: int
