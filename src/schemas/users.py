from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    username: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None


class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True