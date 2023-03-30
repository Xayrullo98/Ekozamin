
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


from functions import products
from schemas.products import ProductCreate,ProductBase,ProductOut

router_product = APIRouter()



@router_product.post('/add', )
def add_product(data: ProductCreate,db: Session=Depends(get_db)):
    return products.insert_product(payload=data,db=db )


@router_product.get('/',  status_code = 200)
def get_products(db: Session = Depends(get_db)):
    return products.get_all_products(db=db)


@router_product.get('/{id}', status_code = 200,)
def get_product(id:int ,db: Session = Depends(get_db)):
    return products.find_product(product_id=id,db=db)


@router_product.patch('/{id}')
def update_product(id: int, payload:ProductBase ,db: Session = Depends(get_db)):
    return products.update_product(product_id=id,payload=payload,db=db)

# @router_product.put('/{id}')
# def update_product_kpi(id: int, payload:productBase ,db: Session = Depends(get_db)):
#     return productClass.update_product(product_id=id,payload=payload,db=db)

