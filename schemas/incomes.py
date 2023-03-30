from pydantic import BaseModel


class IncomeBase(BaseModel):
    money: int
    type: str
    source:str


class IncomeCreate(IncomeBase):
    user_id: int
    source_id: int


class IncomeOut(IncomeBase):
    id: int
