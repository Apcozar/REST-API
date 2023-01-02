from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.session import get_session
from ..schemas.friendships import FriendshipCreate
from ..repository import friendships_repository

router = APIRouter(
    prefix="/friends",
    tags=["friends"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_friend(create_friend: FriendshipCreate, session: Session = Depends(get_session)):
    existing_friend = friendships_repository.get_friend(create_friend.user_id, create_friend.friend_id, session)

    if existing_friend:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {create_friend.user_id} is already friend of user {create_friend.friend_id}")
    
    
    new_friend = friendships_repository.create_friend(create_friend, session)
    return {"data": new_friend}


@router.get("/", status_code=status.HTTP_200_OK)
def get_friends(user_id: int, session: Session = Depends(get_session)):
    friends = friendships_repository.get_friends(user_id, session)
    return {"data": friends}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_friend(friend: FriendshipCreate, session: Session = Depends(get_session)):
    friend = friendships_repository.get_friend(friend.user_id, friend.friend_id, session)

    if friend == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    friendships_repository.delete_friend(friend, session)

    return Response(status_code=status.HTTP_204_NO_CONTENT)