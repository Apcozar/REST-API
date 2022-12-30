from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(
    prefix="/friend",
    tags=["friend"],
)

@router.get("/", status_code=status.HTTP_201_CREATED)
def create_friendship(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    new_friendship = models.Friendship(user_id=user_id, friend_id=friend_id)
    db.add(new_friendship)
    db.commit()
    db.refresh(new_friendship)
    return {"data": new_friendship}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_friends(id: int, db: Session = Depends(get_db)):
    friends = db.query(models.Friendship).filter(models.Friendship.user_id== id).all()
    return {"data": friends}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_friend(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    friendship_query = db.query(models.Friendship).filter(models.Friendship.user_id == user_id and 
        models.Friendship.friend_id == friend_id)

    friendship = friendship_query.first()

    if friendship == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="This users are not friends")

    friendship_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)