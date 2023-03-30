import time

import shutil
from fastapi import HTTPException, UploadFile

from sqlalchemy.orm import Session

from models.uploaded_files import Uploaded_files
from schemas.uploaded_files import Uploaded_fileBase, Uploaded_fileCreate


def get_all_files(db: Session):
    """return a list of all files"""
    return db.query(Uploaded_files).all()


def find_file(file_id: int, db: Session):
    """returns a file that matches the id"""
    file = db.query(Uploaded_files).filter(Uploaded_files.id == file_id).first()

    if not file:
        raise HTTPException

    return file


def insert_file(payload: Uploaded_fileCreate, db: Session,):
    """returns a new file"""
    with open('media/'+payload.file.filename,'wb') as image:
        shutil.copyfileobj(payload.file.file,image)

    file_url = str('media/'+payload.file.filename)
    file = db.query(Uploaded_files).filter(Uploaded_files.file == file_url).first()

    if file:
        raise HTTPException(status_code=400, detail="Uploaded_file already exists!")

    else:
        record = Uploaded_files(file=file_url, source_id=payload.source_id, source=payload.source, user_id=payload.user_id)
        db.add(record)
        db.commit()
        db.refresh(record)
        return record


def update_file(file_id: int, payload: Uploaded_fileBase, db: Session):
    note_query = db.query(Uploaded_files).filter(Uploaded_files.id == file_id)
    db_note = note_query.first()
    update_data = payload.dict()
    note_query.filter(Uploaded_files.id == file_id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_note)
    return db_note