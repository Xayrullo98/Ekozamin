
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import incomes
from schemas.incomes import *

router_income = APIRouter()



@router_income.post('/add', )
def add_income(data: IncomeCreate,db: Session=Depends(get_db)):
    return incomes.insert_income(payload=data,db=db )


@router_income.get('/',  status_code = 200)
def get_incomes(db: Session = Depends(get_db)):
    return incomes.get_all_incomes(db=db)


@router_income.get('/{id}', status_code = 200,)
def get_income(id:int ,db: Session = Depends(get_db)):
    return incomes.find_income(income_id=id,db=db)


@router_income.patch('/{id}')
def update_income(id: int, payload:IncomeBase ,db: Session = Depends(get_db)):
    return incomes.update_income(income_id=id,payload=payload,db=db)

# @router_income.put('/{id}')
# def update_income_kpi(id: int, payload:incomeBase ,db: Session = Depends(get_db)):
#     return incomeClass.update_income(income_id=id,payload=payload,db=db)