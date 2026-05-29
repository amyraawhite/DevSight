from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import UserCreate

from ..auth import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

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

    print(f"REGISTER DB ID: {id(db)}")

    users = db.query(User).all()
    print(f"USERS AFTER REGISTER: {users}")

    db.refresh(new_user)

    return {"message" : "User registered successfully"}

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=400,
            detail="User not found."
        )

    if not verify_password(
        form_data.password,
        existing_user.hashed_password
    ):

        raise HTTPException(
            status_code=400,
            detail="Incorrect password."
        )

    token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"  # nosec B105
    }