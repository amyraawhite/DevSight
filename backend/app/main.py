from fastapi import FastAPI
from .database import engine
from .models import Base

# Creates all tables specified in models.py if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root(): 
    return {
        "message": "DevSight API Running"
    }