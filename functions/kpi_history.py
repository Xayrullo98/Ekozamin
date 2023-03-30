from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.kpi_history import Kpi_History
from schemas.kpi_history import Kpi_HistoryCreate,Kpi_HistoryBase


def get_all_kpi_history(db: Session):
	"""return a list of all Kpi_History"""
	return db.query(Kpi_History).all()


def find_kpi_history(kpi_history_id: int, db: Session):
	"""returns a kpi_history that matches the id"""
	kpi_history = db.query(Kpi_History).filter(Kpi_History.id == kpi_history_id).first()
	
	if not kpi_history:
		raise HTTPException
	
	return kpi_history


def insert_kpi_history(payload: Kpi_HistoryCreate, db: Session):
	"""returns a new kpi_history"""
	record = Kpi_History(money=payload.money, user_id=payload.user_id,
	                comment=payload.comment,trade_id = payload.trade_id )
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_kpi_history(kpi_history_id: int, payload: Kpi_HistoryBase, db: Session):
	note_query = db.query(Kpi_History).filter(Kpi_History.id == kpi_history_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Kpi_History.id == kpi_history_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note