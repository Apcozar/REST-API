from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True