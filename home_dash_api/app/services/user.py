from app.models.user import User
from app.schemas.user import UserSchema


async def get_user_by_email(email: str):
    user = await User.filter(email=email).first()

    return UserSchema.from_orm(user) if user else None


async def get_current_user():
    return await get_user_by_email("jim@justjibba.net")
