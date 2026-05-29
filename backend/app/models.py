"""
Database ORM models. 

These python classes map directly to PostgreSQL database tables 
"""

# SLQAlchemy coln/data types 
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


from datetime import datetime, timezone

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
    hashed_password = Column(String)

    projects = relationship(
        "Project",
        back_populates="owner"
    )


class Project(Base): 
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)

    description = Column(String)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="projects"
    )

