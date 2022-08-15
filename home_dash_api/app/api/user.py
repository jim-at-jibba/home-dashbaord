from app.schemas.user import UserSchema
from app.services.user import get_current_user
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/api/users/me", response_model=UserSchema)
async def get_user(user: UserSchema = Depends(get_current_user)):
    return user
