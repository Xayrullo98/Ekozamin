
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import uploaded_files
from schemas.uploaded_files import *

router_uploaded_file = APIRouter()



@router_uploaded_file.post('/add', )
def add_uploaded_file(data: Uploaded_fileCreate,db: Session = Depends(get_db)):
    return uploaded_files.insert_file(payload=data,db=db)


@router_uploaded_file.get('/',  status_code = 200)
def get_uploaded_files(db: Session = Depends(get_db)):
    return uploaded_files.get_all_files(db=db)


@router_uploaded_file.get('/{id}', status_code = 200,)
def get_uploaded_file(id:int ,db: Session = Depends(get_db)):
    return uploaded_files.find_file(file_id=id,db=db)


@router_uploaded_file.patch('/{id}')
def update_uploaded_file(id: int, payload:Uploaded_fileBase ,db: Session = Depends(get_db)):
    return uploaded_files.update_file(file_id=id,payload=payload,db=db)

# @router_uploaded_file.put('/{id}')
# def update_uploaded_file_kpi(id: int, payload:uploaded_fileBase ,db: Session = Depends(get_db)):
#     return uploaded_fileClass.update_uploaded_file(uploaded_file_id=id,payload=payload,db=db)