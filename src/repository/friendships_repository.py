from sqlalchemy.orm import Session
from .. import models, schemas


def create_friend(create_friend: schemas.Friendships, db: Session):
    new_friendship = models.Friendships(user_id=create_friend.user_id, 
                            friend_id=create_friend.friend_id)

    db.add(new_friendship)
    db.commit()
    db.refresh(new_friendship)
    return new_friendship


def get_friends(id: int, db: Session):
    return db.query(models.Friendships).filter(models.Friendships.user_id==id).all()


def get_friend(user_id: int, friend_id: int, db: Session):
    return db.query(models.Friendships).filter(models.Friendships.user_id==user_id,
                    models.Friendships.friend_id==friend_id).first()
   

def delete_friend(delete_friend: schemas.Friendships, db: Session):
    db.delete(delete_friend)
    db.commit()
    db.flush()
