from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greeting():
    return {
        'Ganesh': 'Cool',
        'Krutika': 'Loser',
        'Life': 'Good'
    }
