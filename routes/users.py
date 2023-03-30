
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import users
from schemas.users import *

router_user = APIRouter()



@router_user.post('/add', )
def add_user(data: UserCreate,db: Session=Depends(get_db)):
    return users.insert_user(payload=data,db=db )


@router_user.get('/',  status_code = 200)
def get_users(db: Session = Depends(get_db)):
    return users.get_all_users(db=db)


@router_user.get('/{id}', status_code = 200,)
def get_user(id:int ,db: Session = Depends(get_db)):
    return users.find_user(user_id=id,db=db)


# @router_user.patch('/{id}')
# def update_user(id: int, payload:UserBase ,db: Session = Depends(get_db)):
#     return users.(user_id=id,payload=payload,db=db)

# @router_user.put('/{id}')
# def update_user_kpi(id: int, payload:userBase ,db: Session = Depends(get_db)):
#     return userClass.update_user(user_id=id,payload=payload,db=db)

