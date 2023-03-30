
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.orders import Orders
from schemas.orders import OrderBase, OrderCreate


def get_all_orders(db: Session):
	"""return a list of all orders"""
	return db.query(Orders).all()


def find_order(order_id: int, db: Session):
	"""returns a order that matches the id"""
	order = db.query(Orders).filter(Orders.id == order_id).first()
	
	if not order:
		raise HTTPException
	
	return order


def insert_order(payload: OrderCreate, db: Session):
	"""returns a new order"""
	record = Orders(customer_id=payload.customer_id, user_id=payload.user_id,
	                  comment=payload.comment, )
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_order(order_id: int, payload: OrderBase, db: Session):
	note_query = db.query(Orders).filter(Orders.id == order_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Orders.id == order_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note