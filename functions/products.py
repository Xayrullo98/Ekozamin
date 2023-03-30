import time

from fastapi import HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from db import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from models.products import Products
from schemas.products import ProductBase, ProductCreate


def get_all_products(db: Session):
	"""return a list of all products"""
	return db.query(Products).all()


def find_product(product_id: int, db: Session):
	"""returns a product that matches the id"""
	product = db.query(Products).filter(Products.id == product_id).first()
	
	if not product:
		raise HTTPException
	
	return product


def insert_product(payload: ProductCreate, db: Session):
	"""returns a new product"""
	record = Products(name=payload.name, price=payload.price, user_id=payload.user_id,
	                comment=payload.comment, birlik=payload.birlik)
	db.add(record)
	db.commit()
	db.refresh(record)
	
	return record

def update_product(product_id: int,payload:  ProductBase, db: Session):
	note_query = db.query(Products).filter(Products.id == product_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Products.id == product_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note