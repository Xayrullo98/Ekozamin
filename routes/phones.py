
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import phones
from schemas.phones import *

router_phone = APIRouter()



@router_phone.post('/add', )
def add_phone(data: PhoneCreate,db: Session=Depends(get_db)):
    return phones.insert_phone(payload=data,db=db )


@router_phone.get('/',  status_code = 200)
def get_phones(db: Session = Depends(get_db)):
    return phones.get_all_phones(db=db)


@router_phone.get('/{id}', status_code = 200,)
def get_phone(id:int ,db: Session = Depends(get_db)):
    return phones.find_phone(phone_id=id,db=db)


# @router_phone.patch('/{id}')
# def update_phone(id: int, payload:phoneBase ,db: Session = Depends(get_db)):
#     return phones.(phone_id=id,payload=payload,db=db)

# @router_phone.put('/{id}')
# def update_phone_kpi(id: int, payload:phoneBase ,db: Session = Depends(get_db)):
#     return phoneClass.update_phone(phone_id=id,payload=payload,db=db)

