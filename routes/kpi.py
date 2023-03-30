
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import kpi
from schemas.kpi import *

router_kpi = APIRouter()



@router_kpi.post('/add', )
def add_kpi(data: KpiCreate,db: Session=Depends(get_db)):
    return kpi.insert_kpi(payload=data,db=db )


@router_kpi.get('/',  status_code = 200)
def get_kpis(db: Session = Depends(get_db)):
    return kpi.get_all_kpis(db=db)


@router_kpi.get('/{id}', status_code = 200,)
def get_kpi(id:int ,db: Session = Depends(get_db)):
    return kpi.find_kpi(kpi_id=id,db=db)


@router_kpi.patch('/{id}')
def update_kpi(id: int, payload:KpiBase ,db: Session = Depends(get_db)):
    return kpi.update_kpi(kpi_id=id,payload=payload,db=db)

# @router_kpi.put('/{id}')
# def update_kpi_kpi(id: int, payload:kpiBase ,db: Session = Depends(get_db)):
#     return kpiClass.update_kpi(kpi_id=id,payload=payload,db=db)