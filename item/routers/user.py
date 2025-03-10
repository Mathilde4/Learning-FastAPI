from fastapi import APIRouter, Depends,status, HTTPException, Response
from typing import List
from .. import schemas, models, database
from  sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

get_db = database.get_db
router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session= Depends(get_db)):
    return user.create_user(request,db)



@router.get('/{id}', response_model=schemas.ShowUser, status_code=200)
def get_user(id:int,db: Session= Depends(get_db)):
    return user.get_user(id,db)