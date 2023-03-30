from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.incomes import Incomes
from schemas.incomes import IncomeBase, IncomeCreate


def get_all_incomes(db: Session):
	"""return a list of all incomes"""
	return db.query(Incomes).all()


def find_income(income_id: int, db: Session):
	"""returns a income that matches the id"""
	income = db.query(Incomes).filter(Incomes.id == income_id).first()
	
	if not income:
		raise HTTPException
	
	return income


def insert_income(payload: IncomeCreate, db: Session):
	"""returns a new income"""
	record = Incomes(money=payload.money, user_id=payload.user_id,
	                 source=payload.source, source_id=payload.source_id, type=payload.type)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_income(income_id: int, payload: IncomeBase, db: Session):
	note_query = db.query(Incomes).filter(Incomes.id == income_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Incomes.id == income_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note
