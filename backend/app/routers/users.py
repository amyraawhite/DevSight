from fastapi import APIRouter
from fastapi import Depends

from ..auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
def get_me(current_user=Depends(get_current_user)): 
    return ( {
        "id" : current_user.id,
        "username" : current_user.username,
        "email" : current_user.email
    } )