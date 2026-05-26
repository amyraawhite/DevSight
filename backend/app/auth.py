from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

# =========================
# JWT Configuration
# =========================
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = (os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

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
    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({
        "exp" : expire
    })

    encode_jwt = jwt.encode(
        to_encode, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )

    return encode_jwt