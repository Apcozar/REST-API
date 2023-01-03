from sqlalchemy.orm import Session
from ..models.users import Users
from ..schemas.users_schemas import UserCreate, UserBase
from ..core import security


def create_user(user: UserCreate, session: Session):
    hased_pwd = security.hash(user.password)
    user.password = hased_pwd
    new_user = Users(**user.dict())
                
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def get_users(session: Session):
    return session.query(Users).all()


def get_user(id: int, session: Session):
    return session.query(Users).filter(Users.user_id == id).first()


def get_user_by_username(username: str, session: Session):
    return session.query(Users).filter(Users.username == username).first()


def get_user_by_email(email: str, session: Session):
    return session.query(Users).filter(Users.email == email).first()


def update_user(id: int, updated_user: UserBase, session: Session):
    existing_user = session.query(Users).filter(Users.user_id == id)
    
    if not existing_user.first():
        return None
   
    session.add(updated_user)
    session.commit()
    session.refresh(updated_user)

    return updated_user

def delete_user(user_id: int, session: Session):
    existing_user = session.query(Users).filter(Users.user_id == user_id)

    if not existing_user.first():
        return None

    existing_user.delete(synchronize_session=False)
    session.commit()