
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import customers
from schemas.customers import *

router_customer = APIRouter()



@router_customer.post('/add', )
def add_customer(data: CustomerCreate,db: Session=Depends(get_db)):
    return customers.insert_customer(payload=data,db=db )


@router_customer.get('/',  status_code = 200)
def get_customers(db: Session = Depends(get_db)):
    return customers.get_all_customers(db=db)


@router_customer.get('/{id}', status_code = 200,)
def get_customer(id:int ,db: Session = Depends(get_db)):
    return customers.find_customer(customer_id=id,db=db)


@router_customer.patch('/{id}')
def update_customer(id: int, payload:CustomerBase ,db: Session = Depends(get_db)):
    return customers.update_customer(customer_id=id,payload=payload,db=db)

# @router_customer.put('/{id}')
# def update_customer_kpi(id: int, payload:customerBase ,db: Session = Depends(get_db)):
#     return customerClass.update_customer(customer_id=id,payload=payload,db=db)