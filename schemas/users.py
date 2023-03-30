from typing import Union

from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    roll: str


class UserCreate(UserBase):
    username: str
    password: str


class WorkerOut(UserBase):
    id: int


class Token(BaseModel):
    access_token = str
    token = str


class TokenData(BaseModel):
    id: Optional[str] = None
