from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..hashing import Hash
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix= '/login',
    tags= ['Authentication']
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends() , db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail=f"Incorrect Password")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}