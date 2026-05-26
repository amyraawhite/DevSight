from pydantic import BaseModel, EmailStr

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

    class Config: 
        from_attributes = True

# =========================
# User Token Schema
# =========================
class Token(BaseModel): 
    access_token : str
    token_type : str

