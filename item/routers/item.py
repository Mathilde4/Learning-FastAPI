from fastapi import APIRouter, Depends,status, HTTPException, Response
from typing import List
from .. import schemas, models, database, oauth2
from  sqlalchemy.orm import Session
from ..repository import item



get_db = database.get_db
router = APIRouter(
    prefix='/item',
    tags=['Items']
)


@router.get('/', response_model=List[schemas.ShowItem])
def get_all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Item,db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.create(request, db)
    

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_item(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.delete(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update_item(id:int, request: schemas.Item, db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.update(id,request, db)
    

# @app.get('/item',tags=['items'], response_model=List[schemas.ShowItem])
# def get_all(db: Session = Depends(get_db)):
#     items = db.query(models.Item).all()
#     return items

@router.get('/item/{id}', status_code=200, response_model=schemas.ShowItem)
def get_one(id:int, response : Response ,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.get_one(id, db)
