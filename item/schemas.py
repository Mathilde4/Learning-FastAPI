from pydantic import BaseModel
from typing import List, Optional



class ItemBase(BaseModel):
    title: str
    body:str

class Item(ItemBase):
    pass



class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    items: List[Item] = []


class ShowItem(BaseModel):
    title: str
    body:str
    creator: ShowUser


class Login (BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    