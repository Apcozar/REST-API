from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    username: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None


class UserCreate(UserBase):
    name: str
    surname: str
    username: str
    age: int
    gender: str
    is_admin: Optional[bool] = False


    class Config:
        orm_mode = True

class UserAdminCreate(UserBase):
    name: str
    surname: str
    username: str
    age: int
    gender: str
    is_admin: bool



class UserOut(UserBase):
    user_id: int
    name: str
    surname: str
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True