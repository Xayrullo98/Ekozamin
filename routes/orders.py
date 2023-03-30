
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import orders
from schemas.orders import *

router_order = APIRouter()



@router_order.post('/add', )
def add_order(data: OrderCreate,db: Session=Depends(get_db)):
    return orders.insert_order(payload=data,db=db )


@router_order.get('/',  status_code = 200)
def get_orders(db: Session = Depends(get_db)):
    return orders.get_all_orders(db=db)


@router_order.get('/{id}', status_code = 200,)
def get_order(id:int ,db: Session = Depends(get_db)):
    return orders.find_order(order_id=id,db=db)


@router_order.patch('/{id}')
def update_order(id: int, payload:OrderBase ,db: Session = Depends(get_db)):
    return orders.update_order(order_id=id,payload=payload,db=db)

# @router_order.put('/{id}')
# def update_order_kpi(id: int, payload:orderBase ,db: Session = Depends(get_db)):
#     return orderClass.update_order(order_id=id,payload=payload,db=db)