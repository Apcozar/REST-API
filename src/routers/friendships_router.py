from typing import List
from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session


from ..db.session import get_session
from ..schemas.friendships_schemas import FriendshipBase
from ..repository import friendships_repository, users_repository
from ..core.security import get_current_user

router = APIRouter(
    prefix="/friendships",
    tags=["friendships"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FriendshipBase)
def create_friendship(create_friendship: FriendshipBase, session: Session = Depends(get_session), 
    cur_user: int = Depends(get_current_user)):

    existing_user = users_repository.get_user(create_friendship.user_id, session)
    existing_friend = users_repository.get_user(create_friendship.friend_id, session)

    if not existing_friend or not cur_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {existing_friend.used_id} does not exist")

    if existing_user.user_id != cur_user.user_id and not cur_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You cannot create relationships for other people")

    existing_friendship = friendships_repository.get_friendship(
        create_friendship.user_id, create_friendship.friend_id, session)

    if existing_friendship:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"user {create_friendship.user_id} is already friend of user {create_friendship.friend_id}")
    
    new_friendship = friendships_repository.create_friendship(create_friendship, session)
    return  new_friendship


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=List[FriendshipBase])
def get_friendships(id: int, session: Session = Depends(get_session), 
    cur_user: int = Depends(get_current_user)):

    friendships = friendships_repository.get_friendships(id, session)
    return friendships


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_friendship(delete_friendship: FriendshipBase, session: Session = Depends(get_session), 
    cur_user: int = Depends(get_current_user)):

    existing_friendship = friendships_repository.get_friendship(delete_friendship.user_id, 
                            delete_friendship.friend_id, session)

    if not existing_friendship or not cur_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {delete_friendship.user_id} is not friend of user {delete_friendship.friend_id}")

    if existing_friendship.user_id != cur_user.user_id and not cur_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not in this friendship")

    friendships_repository.delete_friendship(delete_friendship, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)