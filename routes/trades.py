
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import trades
from schemas.trades import TradeCreate,TradeBase,TradeOut

router_trade = APIRouter()



@router_trade.post('/add', )
def add_trade(data: TradeCreate,db: Session = Depends(get_db)):
    return trades.insert_trade(payload=data,db=db )


@router_trade.get('/',  status_code = 200)
def get_trades(db: Session = Depends(get_db)):
    return trades.get_all_trades(db=db)


@router_trade.get('/{id}', status_code = 200,)
def get_trade(id:int ,db: Session = Depends(get_db)):
    return trades.find_trade(trade_id=id,db=db)


@router_trade.patch('/{id}')
def update_trade(id: int, payload:TradeBase ,db: Session = Depends(get_db)):
    return trades.update_trade(trade_id=id,payload=payload,db=db)

 

