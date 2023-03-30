
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.trades import Trades
from schemas.trades import TradeBase, TradeCreate


def get_all_trades(db: Session):
	"""return a list of all trades"""
	return db.query(Trades).all()


def find_trade(trade_id: int, db: Session):
	"""returns a trade that matches the id"""
	trade = db.query(Trades).filter(Trades.id == trade_id).first()
	
	if not trade:
		raise HTTPException
	
	return trade


def insert_trade(payload: TradeCreate, db: Session):
	"""returns a new trade"""
	record = Trades(quantity=payload.quantity, price=payload.price, user_id=payload.user_id,
	                  order_id=payload.order_id, product_id=payload.product_id,)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record


def update_trade(trade_id: int, payload: TradeBase, db: Session):
	note_query = db.query(Trades).filter(Trades.id == trade_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Trades.id == trade_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note