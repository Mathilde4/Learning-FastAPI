from typing import Optional
from fastapi import FastAPI
import uvicorn
from colorama import init
from pydantic import BaseModel

app = FastAPI()

@app.get("/item")
def index(limit=10, published:bool =True, sort : Optional[str] = None):

    if published:
        return {"data": f"{limit} published items from the db"}
    else:
        return {"data": f"{limit} items from the db"}
    

@app.get("/item/unplublished")
def unplublished():
    return {'data': 'all unplublished items'}

@app.get("/item/{id}")
def item(id:int):
    # fetch item with id = id
    return {'data': id}

@app.get("/item/{id}/comments")
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class item(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]  

@app.post("/item")
def create_item(item : item): 
    return {'data': f'Item is created with title as {item.title}'}


if __name__ == '__main__':
    init()
    uvicorn.run(app, host="127.0.0.1", port = 8000)