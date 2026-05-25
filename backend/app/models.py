"""
Database ORM models. 

These python classes map directly to PostgreSQL database tables 
"""

# SLQAlchemy coln/data types 
from sqlalchemy import Column, Integer, String

# Import ORM base class 
from .database import Base 

"""
User database table. 

Reach instance of User represents one row in the users table
"""
class User(Base): 
    # name of the PostgreSQL table 
    __tablename__ = "users"

    """
    Primary key user ID

    Integer: 
    - Automatically increments
    - Uniquely identifies each user
    """
    id = Column(Integer, primary_key=True, index=True)

    """
    Unique username for login/display.
    """
    username = Column(String, unique=True, index=True)

    """
    Unique email address
    """
    email = Column(String, unique=True, index=True)

    """
    Stores hashed password. 
    """
    hashed_password = Column(String).