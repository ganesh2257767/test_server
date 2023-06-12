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
    return {
        'result': f'{item.name} with desciption {item.description} and price {item.price} added successfully',
        'note': 'No database initialized so no data is actually being added, only simulated.'
        }
    