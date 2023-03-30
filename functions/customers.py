import time

from fastapi import HTTPException

from sqlalchemy.orm import Session

from models.customers import Customers
from schemas.customers import CustomerBase,CustomerCreate


    
def get_all_customers(db: Session):
        """return a list of all customers"""
        return db.query(Customers).all()

    
def find_customer(customer_id: int, db: Session):

        """returns a customer that matches the id"""
        customer = db.query(Customers).filter(Customers.id == customer_id).first()

        if not customer:
            raise HTTPException

        return customer

    
def insert_customer(payload: CustomerCreate, db: Session):
        """returns a new customer"""
        customer = db.query(Customers).filter(Customers.name == payload.name).first()

        if customer:
            raise HTTPException(status_code=400, detail="Customer already exists!")

        else:
            record = Customers(name=payload.name,address=payload.address,comment=payload.comment,user_id=payload.user_id)
            db.add(record)
            db.commit()
            db.refresh(record)
            return record


    
def update_customer(customer_id: int,payload:  CustomerBase, db: Session):
        note_query = db.query(Customers).filter(Customers.id == customer_id)
        db_note = note_query.first()
        update_data = payload.dict()
        note_query.filter(Customers.id == customer_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_note)
        return db_note