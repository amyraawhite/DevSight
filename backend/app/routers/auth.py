from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate
from ..schemas import UserLogin

from ..auth import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# =========================
# Database Dependency
# =========================
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally: 
        db.close()

# =========================
# Register Endpoint
# =========================
@router.post("/register")
def register(user : UserCreate, db : Session = Depends(get_db)): 
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    hashed_pw = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message" : "User registered successfully"}

@router.post("/login")
def login(user : UserLogin, db : Session = Depends(get_db)): 
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user: 
        raise HTTPException(
            status_code=400,
            detail="User not found."
        )
    elif not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )


    token = create_access_token(
        data={
            "sub" : existing_user.email
        }
    )
    return {
        "access_token" : str(token),
        "token_type" : "bearer"
    }
    
