import datetime as dt
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        orm_mode = True
