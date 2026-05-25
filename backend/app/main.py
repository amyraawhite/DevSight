from fastapi import FastAPI
from .database import engine
from .models import Base

app = FastAPI()

@app.on_event("startup")
def startup():
    # Creates all tables specified in models.py if they don't exist
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root(): 
    return {
        "message": "DevSight API Running"
    }