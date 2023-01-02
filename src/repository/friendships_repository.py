from sqlalchemy.orm import Session
from ..schemas.friendships import FriendshipCreate
from ..models.friendships import Friendships


def create_friend(create_friend: FriendshipCreate, session: Session):
    new_friendship = Friendships(user_id=create_friend.user_id, 
                            friend_id=create_friend.friend_id)

    session.add(new_friendship)
    session.commit()
    session.refresh(new_friendship)
    return new_friendship


def get_friends(id: int, session: Session):
    return session.query(Friendships).filter(Friendships.user_id==id).all()


def get_friend(user_id: int, friend_id: int, session: Session):
    return session.query(Friendships).filter(Friendships.user_id==user_id,
                    Friendships.friend_id==friend_id).first()
   

def delete_friend(delete_friend: FriendshipCreate, session: Session):
    session.delete(delete_friend)
    session.commit()
    session.flush()
