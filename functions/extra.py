from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.extra import Extra
from schemas.extra import ExtraBase, ExtraCreate


def get_all_extras(db: Session):
	"""return a list of all extras"""
	return db.query(Extra).all()


def find_extra(extra_id: int, db: Session):
	"""returns a extra that matches the id"""
	extra = db.query(Extra).filter(Extra.id == extra_id).first()
	
	if not extra:
		raise HTTPException
	
	return extra


def insert_extra(payload: ExtraCreate, db: Session):
	"""returns a new extra"""
	record = Extra(money=payload.money, user_id=payload.user_id,
	                 source=payload.source, source_id=payload.source_id, type=payload.type)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_extra(extra_id: int, payload: ExtraBase, db: Session):
	note_query = db.query(Extra).filter(Extra.id == extra_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Extra.id == extra_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note
