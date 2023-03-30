
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import kpi_history
from schemas.kpi_history import *

router_kpi_history = APIRouter()



@router_kpi_history.post('/add', )
def add_kpi_history(data: Kpi_HistoryCreate,db: Session=Depends(get_db)):
    return kpi_history.insert_kpi_history(payload=data,db=db )


@router_kpi_history.get('/',  status_code = 200)
def get_kpi_historys(db: Session = Depends(get_db)):
    return kpi_history.get_all_kpi_history(db=db)


@router_kpi_history.get('/{id}', status_code = 200,)
def get_kpi_history(id:int ,db: Session = Depends(get_db)):
    return kpi_history.find_kpi_history(kpi_history_id=id,db=db)


@router_kpi_history.patch('/{id}')
def update_kpi_history(id: int, payload:Kpi_HistoryBase ,db: Session = Depends(get_db)):
    return kpi_history.update_kpi_history(kpi_history_id=id,payload=payload,db=db)

# @router_kpi_history.put('/{id}')
# def update_kpi_history_kpi(id: int, payload:kpi_historyBase ,db: Session = Depends(get_db)):
#     return kpi_historyClass.update_kpi_history(kpi_history_id=id,payload=payload,db=db)