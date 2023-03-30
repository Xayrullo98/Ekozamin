from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.expenses import Expenses
from schemas.expenses import ExpenseBase, ExpenseCreate


def get_all_expenses(db: Session):
	"""return a list of all expenses"""
	return db.query(Expenses).all()


def find_expense(expense_id: int, db: Session):
	"""returns a expense that matches the id"""
	expense = db.query(Expenses).filter(Expenses.id == expense_id).first()
	
	if not expense:
		raise HTTPException
	
	return expense


def insert_expense(payload: ExpenseCreate, db: Session):
	"""returns a new expense"""
	record = Expenses(money=payload.money, user_id=payload.user_id,
	                 source=payload.source, source_id=payload.source_id, type=payload.type)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_expense(expense_id: int, payload: ExpenseBase, db: Session):
	note_query = db.query(Expenses).filter(Expenses.id == expense_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Expenses.id == expense_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note
