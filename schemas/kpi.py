from pydantic import BaseModel


class KpiBase(BaseModel):
    percentage: int
    role: str


class KpiCreate(KpiBase):
    user_id: int


class KpiOut(KpiBase):
    id: int
