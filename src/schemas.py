from pydantic import BaseModel

class OutUser(BaseModel):
    name: str
    surname: str
    description: str
    
    class Config:
        orm_mode = True


class InUser(BaseModel):
    name: str
    surname: str
    description: str

    class Config:
        orm_mode = True

class InFriend(BaseModel):
    user_id: int
    friend_id: int

    class Config:
        orm_mode = True
