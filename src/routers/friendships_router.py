from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.session import get_session
from ..schemas.friendships import FriendshipBase
from ..repository import friendships_repository

router = APIRouter(
    prefix="/friendships",
    tags=["friendships"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_friendship(create_friendship: FriendshipBase, session: Session = Depends(get_session)):
    existing_friendship = friendships_repository.get_friendship(create_friendship.user_id, create_friendship.friend_id, session)

    if existing_friendship:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {create_friendship.user_id} is already friend of user {create_friendship.friend_id}")
    
    new_friendship = friendships_repository.create_friendship(create_friendship, session)
    return {"data": new_friendship}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_friendships(id: int, session: Session = Depends(get_session)):
    friendships = friendships_repository.get_friendships(id, session)
    return {"data": friendships}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_friendship(delete_friendship: FriendshipBase, session: Session = Depends(get_session)):
    existing_friendship = friendships_repository.get_friendship(delete_friendship.user_id, 
                            delete_friendship.friend_id, session)

    if not existing_friendship:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {user_id} is not friend of user {friend_id}")

    friendships_repository.delete_friendship(delete_friendship, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)