from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..schemas.friendships import FriendshipCreate
from ..repository import friendships_repository

router = APIRouter(
    prefix="/friends",
    tags=["friends"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_friend(create_friend: FriendshipCreate, db: Session = Depends(get_db)):
    existing_friend = friendships_repository.get_friend(create_friend.user_id, create_friend.friend_id, db)

    if existing_friend:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {create_friend.user_id} is already friend of user {create_friend.friend_id}")
    
    
    new_friend = friendships_repository.create_friend(create_friend, db)
    return {"data": new_friend}


@router.get("/", status_code=status.HTTP_200_OK)
def get_friends(user_id: int, db: Session = Depends(get_db)):
    friends = friendships_repository.get_friends(user_id, db)
    return {"data": friends}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_friend(friend: FriendshipCreate, db: Session = Depends(get_db)):
    friend = friendships_repository.get_friend(friend.user_id, friend.friend_id, db)

    if friend == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    friendships_repository.delete_friend(friend, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)