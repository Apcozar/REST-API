from sqlalchemy.orm import Session
from ..models.users import Users
from ..schemas.users import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = Users(
        name=user.name, 
        surname=user.surname, 
        username=user.username, 
        age=user.age, 
        gender=user.gender)
                
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(Users).all()


def get_user(id: int, db: Session):
    return db.query(Users).filter(Users.user_id == id).first()


def update_user(id: int, updated_user: UserCreate, db: Session):
    existing_user = db.query(Users).filter(Users.user_id == id)
    
    if not existing_user.first():
        return None

    existing_user.update(updated_user.dict(),synchronize_session=False)

    db.commit()

    return updated_user

def delete_user(user_id: int, db: Session):
    existing_user = db.query(Users).filter(Users.user_id == user_id)

    if not existing_user.first():
        return None

    existing_user.delete(synchronize_session=False)
    db.commit()