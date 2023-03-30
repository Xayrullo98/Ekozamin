from typing import Union

from pydantic import BaseModel
from typing import Optional


class PhoneBase(BaseModel):
	number: str
	source: str


class PhoneCreate(PhoneBase):
	comment: Optional[str]
	user_id: int
	source_id: int


class PhoneOut(PhoneBase):
	id: int

