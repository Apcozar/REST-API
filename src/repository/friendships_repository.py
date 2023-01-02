from sqlalchemy.orm import Session
from ..schemas.friendships import FriendshipBase
from ..models.friendships import Friendships


def create_friendship(create_friendship: FriendshipBase, session: Session):
    new_friendship = Friendships(user_id=create_friendship.user_id, 
                            friend_id=create_friendship.friend_id)

    session.add(new_friendship)
    session.commit()
    session.refresh(new_friendship)
    return new_friendship


def get_friendships(id: int, session: Session):
    return session.query(Friendships).filter(Friendships.user_id==id).all()


def get_friendship(user_id: int, friend_id: int, session: Session):
    return session.query(Friendships).filter(Friendships.user_id==user_id,
                    Friendships.friend_id==friend_id).first()
   

def delete_friendship(delete_friendship: FriendshipBase, session: Session):
    existing_friendship = session.query(Friendships).filter(
                            Friendships.user_id==delete_friendship.user_id,
                            Friendships.friend_id==delete_friendship.friend_id)

    if not existing_friendship.first():
        return None
    
    existing_friendship.delete(synchronize_session=False)
    session.commit()
