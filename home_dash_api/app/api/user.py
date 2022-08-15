from app.schemas.user import UserSchema, UserCreate
from app.services.user import get_current_user, get_user_by_email, create_user, create_token, authenticate_user
from fastapi import APIRouter, Depends, HTTPException
import fastapi.security as security


router = APIRouter()


@router.post("/api/users")
async def user_create(user: UserCreate):
    db_user = await get_user_by_email(user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use.")

    user = await create_user(user)

    return await create_token(user)


@router.post("/api/token")
async def generate_token(form_data: security.OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return await create_token(user)


@router.get("/api/users/me", response_model=UserSchema)
async def get_me(user: UserSchema = Depends(get_current_user)):
    return user
