from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get('/')
def greeting():
    return {
        'Ganesh': 'Cool',
        'Krutika': 'Loser',
        'Life': 'Good'
    }

@app.post('/')
def add(item: Item):
    return item | {"result": "Item added successfully!"}
    