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
        "from_attribute" : True 
    }

# =========================
# Project Create Schema
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
        "from_attribute" : True 
    }

class ProjectUpdate(BaseModel):
    name : str | None = None
    description : str | None = None 

# =========================
# User Token Schema
# =========================
class Token(BaseModel): 
    access_token : str
    token_type : str

