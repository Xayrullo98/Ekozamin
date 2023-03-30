
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import expenses
from schemas.expenses import *

router_expense = APIRouter()



@router_expense.post('/add', )
def add_expense(data: ExpenseCreate,db: Session=Depends(get_db)):
    return expenses.insert_expense(payload=data,db=db )


@router_expense.get('/',  status_code = 200)
def get_expenses(db: Session = Depends(get_db)):
    return expenses.get_all_expenses(db=db)


@router_expense.get('/{id}', status_code = 200,)
def get_expense(id:int ,db: Session = Depends(get_db)):
    return expenses.find_expense(expense_id=id,db=db)


@router_expense.patch('/{id}')
def update_expense(id: int, payload:ExpenseBase ,db: Session = Depends(get_db)):
    return expenses.update_expense(expense_id=id,payload=payload,db=db)

# @router_expense.put('/{id}')
# def update_expense_kpi(id: int, payload:expenseBase ,db: Session = Depends(get_db)):
#     return expenseClass.update_expense(expense_id=id,payload=payload,db=db)