from pydantic import BaseModel


class CustomerBase(BaseModel):
	name: str
	address: str


class CustomerCreate(CustomerBase):
	comment: str
	user_id: int


class CustomerOut(CustomerBase):
	id: int
