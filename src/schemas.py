from pydantic import BaseModel


class Users(BaseModel):
    name: str
    surname: str
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True

class Friendships(BaseModel):
    user_id: int
    friend_id: int

    class Config:
        orm_mode = True
