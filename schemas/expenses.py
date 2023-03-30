from pydantic import BaseModel


class ExpenseBase(BaseModel):
    money: int
    type: str
    source: str


class ExpenseCreate(ExpenseBase):
    user_id: int
    source_id: int


class ExpenseOut(ExpenseBase):
    id: int
