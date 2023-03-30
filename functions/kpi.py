from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.kpi import Kpi
from schemas.kpi import KpiBase, KpiCreate


def get_all_kpis(db: Session):
	"""return a list of all kpis"""
	return db.query(Kpi).all()


def find_kpi(kpi_id: int, db: Session):
	"""returns a kpi that matches the id"""
	kpi = db.query(Kpi).filter(Kpi.id == kpi_id).first()
	
	if not kpi:
		raise HTTPException
	
	return kpi


def insert_kpi(payload: KpiCreate, db: Session):
	"""returns a new kpi"""
	record = Kpi(role=payload.role, user_id=payload.user_id,
	                percentage=payload.percentage, )
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_kpi(kpi_id: int, payload: KpiBase, db: Session):
	note_query = db.query(Kpi).filter(Kpi.id == kpi_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Kpi.id == kpi_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note