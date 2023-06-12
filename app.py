from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def greeting():
    return {
        'Ganesh': 'Cool',
        'Krutika': 'Loser',
        'Life': 'Good'
    }
    
if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', reload=True)