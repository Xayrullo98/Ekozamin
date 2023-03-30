from pydantic import BaseModel
from typing import Optional


class ExtraBase(BaseModel):
	money: int
	type: str
	source: str


class ExtraCreate(ExtraBase):
	user_id: int
	source_id: int
	


class ExtraOut(ExtraBase):
	id: int
