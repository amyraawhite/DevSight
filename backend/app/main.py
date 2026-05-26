"""
Main FastAPI application entry point.

This file: 
- Creates the FastAPI
- initializes database tables
- defines API routes
- serves as the backend startup file
"""

# import FastAPI framework 
from fastapi import FastAPI

# Import databse engine
from .database import engine

# Import SQLAlchemy base model metadata 
from .models import Base

# Import API routes from routers 
from .routers import auth

# create FastAPI application instance 
app = FastAPI()
app.include_router(auth.router)

"""
Runs when the backend server starts.

Base.metadata.create_all(): 
- inspects all SQLAlchemy models
- generates corresponding database tables 
- creates tables if they do not already exist

bind=engine tells SQLAlchemy which database connection to use 
"""
@app.on_event("startup")
def startup():
    # Creates all tables specified in models.py if they don't exist
    Base.metadata.create_all(bind=engine)

"""
Basic root API endpoint. 

Used to verify: 
- backend is running 
- routing works correctly 
"""
@app.get("/")
def root(): 
    return {
        "message": "DevSight API Running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}


