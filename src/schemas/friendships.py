from typing import Optional
from pydantic import BaseModel


class FriendshipBase(BaseModel):
    user_id: Optional[int] = None
    friend_id: Optional[int] = None

class FriendshipCreate(BaseModel):
    user_id: int
    friend_id: int

    class Config:
        orm_mode = True