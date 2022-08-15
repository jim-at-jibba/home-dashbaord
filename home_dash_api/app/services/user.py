from app.models.user import User
import jwt
from app.schemas.user import UserSchema, UserCreate
from fastapi.encoders import jsonable_encoder
import fastapi.security as security
import passlib.hash as hash
from fastapi import Depends, HTTPException

JWT_SECRET = "areallysecuresecret" # put in env
oauth2schema = security.OAuth2PasswordBearer(tokenUrl="/api/token")



async def create_user(user: UserCreate):
    user_obj = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash.bcrypt.hash(user.password)
    )

    await user_obj.save()
    return user_obj


async def create_token(user: User):
    user_obj = UserSchema.from_orm(user)
    json_compat = jsonable_encoder(user_obj)

    token = jwt.encode(json_compat, JWT_SECRET)

    return dict(access_token=token, token_types="bearer")


async def authenticate_user(email: str, password: str):
    user = await get_user_by_email(email)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user


async def get_user_by_email(email: str):
    return await User.filter(email=email).first()


async def get_current_user(token: str = Depends(oauth2schema)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = await User.filter(id=payload["id"]).first()
    except:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return UserSchema.from_orm(user)

