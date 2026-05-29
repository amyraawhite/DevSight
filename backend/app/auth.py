from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

import os
from dotenv import load_dotenv

from sqlalchemy.orm import Session

from .database import get_db
from .models import User
# =========================
# JWT Configuration
# =========================
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = (os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# =========================
# Password Hashing Context
# =========================
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# =========================
# Hash Password
# =========================
def hash_password(password : str): 
    return pwd_context.hash(password)


# =========================
# Verify Password
# =========================
def verify_password(plain_password : str, hashed_password : str): 
    return pwd_context.verify(plain_password, hashed_password)


# =========================
# Create JWT Access Token
# =========================
def create_access_token(data : dict): 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({
        "exp" : expire
    })

    encode_jwt = jwt.encode(
        to_encode, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )

    return encode_jwt


# =========================
# Get Current Authenticated User
# =========================
def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try: 
        payload = jwt.decode(
            token, 
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print(f"PAYLOAD: {payload}")

        email = payload.get("sub")

        print(f"EMAIL: {email}")

        if email is None: 
            raise credentials_exception
        
    except JWTError as e: 
        print(f"JWT ERROR: {e}")
        raise credentials_exception

    print(f"DB ID: {id(db)}")

    users = db.query(User).all()
    print(f"ALL USERS: {users}")

    user = db.query(User).filter(
        User.email == email
    ).first()

    print(f"USER: {user}")

    if user is None: 
        raise credentials_exception
    

    return user