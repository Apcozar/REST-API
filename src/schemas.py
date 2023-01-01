from pydantic import BaseModel


class Users(BaseModel):
    name: str
    surname: str
    description: str

    class Config:
        orm_mode = True

class Friendships(BaseModel):
    user_id: int
    friend_id: int

    class Config:
        orm_mode = True
