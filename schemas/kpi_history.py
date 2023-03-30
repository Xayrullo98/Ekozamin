from pydantic import BaseModel
from typing import Optional


class Kpi_HistoryBase(BaseModel):
    money: int
    trade_id: int
    comment: Optional[str]


class Kpi_HistoryCreate(Kpi_HistoryBase):
    user_id: int



class Kpi_HistoryOut(Kpi_HistoryBase):
    id: int
