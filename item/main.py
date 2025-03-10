from fastapi import  FastAPI
from . import  models
from  .database import engine, get_db
from  sqlalchemy.orm import Session
from .routers import item, user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(item.router)
app.include_router(user.router)










