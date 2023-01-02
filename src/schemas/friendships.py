from pydantic import BaseModel


class FriendshipBase(BaseModel):
    user_id: int
    friend_id: int

    class Config:
        orm_mode = True