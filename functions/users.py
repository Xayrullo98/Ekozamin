import time

from fastapi import HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from db import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from models.users import Users
from schemas.users import UserBase, UserCreate

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def get_all_users(db: Session):
	"""return a list of all users"""
	return db.query(Users).all()


def find_user(user_id: int, db: Session):
	"""returns a user that matches the id"""
	user = db.query(Users).filter(Users.id == user_id).first()
	
	if not user:
		raise HTTPException(status_code=400, detail="User does not exist!")
	
	return user


def insert_user(payload: UserCreate, db: Session):
	"""returns a new user"""
	user = db.query(Users).filter(Users.username == payload.username).first()
	
	if user:
		raise HTTPException(status_code=400, detail="User already exists!")
	
	else:
		data = {"username": payload.username}
		data.update({'exp': time.time() + ACCESS_TOKEN_EXPIRE_MINUTES}
		            )
		token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
		record = Users(username=payload.username, name=payload.name,
		               roll=payload.roll, password=pwd_context.hash(payload.password), token=token)
		db.add(record)
		db.commit()
		db.refresh(record)
		return record

def delete_user(user_id:int,db:Session):
	user = db.query(Users).filter(Users.id==user_id).first()
	
	if not user:
		raise HTTPException(status_code=400, detail="User does not exist!")
	user = db.query(Users).filter(Users.id == user_id).update({'status':False}, synchronize_session=False)
	db.commit()
	db.refresh(user)
	return {"Done!"}
	

def update_user(order_id: int, payload: UserBase, db: Session):
	note_query = db.query(Users).filter(Users.id == order_id)
	db_note = note_query.first()
	update_data = payload.dict()
	note_query.filter(Users.id == order_id).update(update_data, synchronize_session=False)
	db.commit()
	db.refresh(db_note)
	return db_note