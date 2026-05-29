from pydantic import BaseModel, EmailStr
from datetime import datetime
# =========================
# User Registration Schema
# =========================
class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str

# =========================
# User Login Schema
# =========================
class UserLogin(BaseModel): 
    email : EmailStr
    password : str

# =========================
# User Reponse Schema
# =========================
class UserResponse(BaseModel): 
    id : int
    username : str
    email : EmailStr

    model_config = {
        "from_attributes" : True 
    }

# =========================
# Project Schemas
# =========================
class ProjectCreate(BaseModel): 
    name : str
    description : str

class ProjectResponse(BaseModel): 
    id : int
    name : str
    description : str
    created_at: datetime
    owner_id : int 

    model_config = {
        "from_attributes" : True 
    }

class ProjectUpdate(BaseModel):
    name : str | None = None
    description : str | None = None 

# =========================
# Task Schemas
# =========================
class TaskCreate(BaseModel): 
    title : str
    description : str
    status : str
    priority : str

class TaskResponse(BaseModel): 
    id : int
    title : str
    description : str
    status : str
    priority : str
    created_at : datetime
    project_id : int

    model_config = {
        "from_attributes" : True 
    }


class TaskUpdate(BaseModel): 
    title : str | None = None
    description : str | None = None
    status : str | None = None
    priority : str  | None = None

# =========================
# User Token Schema
# =========================
class Token(BaseModel): 
    access_token : str
    token_type : str

