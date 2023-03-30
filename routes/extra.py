
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import extra
from schemas.extra import *

router_extra = APIRouter()



@router_extra.post('/add', )
def add_extra(data: ExtraCreate,db: Session=Depends(get_db)):
    return extra.insert_extra(payload=data,db=db )


@router_extra.get('/',  status_code = 200)
def get_extras(db: Session = Depends(get_db)):
    return extra.get_all_extras(db=db)


@router_extra.get('/{id}', status_code = 200,)
def get_extra(id:int ,db: Session = Depends(get_db)):
    return extra.find_extra(extra_id=id,db=db)


@router_extra.patch('/{id}')
def update_extra(id: int, payload:ExtraBase ,db: Session = Depends(get_db)):
    return extra.update_extra(extra_id=id,payload=payload,db=db)

# @router_extra.put('/{id}')
# def update_extra_kpi(id: int, payload:extraBase ,db: Session = Depends(get_db)):
#     return extraClass.update_extra(extra_id=id,payload=payload,db=db)