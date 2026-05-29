"""
Database configuration file

Responsible for: 
- creating databse connection 
- configuring SQLAlchemy
- generating database sessions
- defining ORM base class 
"""

# SQLAlchemy database engine utilities 
from sqlalchemy import create_engine 

# SQLAlchemy ORM utilities 
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv


load_dotenv()

"""
Database connection string 

Format: 
postgresql://username:password@host:port/database_name
"""

DATABASE_URL = os.getenv("DATABASE_URL")

"""
Create SQLAlchemy engine 

The engine: 
- database connections 
- SQL execution
- connection pooling
"""

engine = create_engine(DATABASE_URL)


"""
Session factory

Creates independent database sessions 
for interacting with the database

Each request will eventually use its own sessions 
"""

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

"""
Base class for all ORM models. 

Every database model with inherit from Base

SQLAlchemy uses this metadata to: 
- track models
- generate tables 
- manage schema defintions 
"""

Base = declarative_base()


# =========================
# Database Dependency
# =========================
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally: 
        db.close()