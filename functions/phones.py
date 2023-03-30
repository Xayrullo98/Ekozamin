import time

from fastapi import HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from db import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from models.phones import Phones
from schemas.phones import PhoneBase, PhoneCreate


def get_all_phones(db: Session):
	"""return a list of all phones"""
	return db.query(Phones).filter(Phones.status== True).all()


def find_phone(phone_id: int, db: Session):
	"""returns a phone that matches the id"""
	worker = db.query(Phones).filter(Phones.id == phone_id).first()
	
	if not worker:
		raise HTTPException
	
	return worker


def insert_phone(payload: PhoneCreate, db: Session):
	"""returns a new phone"""
	record = Phones(number=payload.number, source=payload.source, user_id=payload.user_id,
	                comment=payload.comment, source_id=payload.source_id)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_phone(phone_id: int, payload: PhoneBase, db: Session):
	note_query = db.query(Phones).filter(Phones.id == phone_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Phones.id == phone_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note
