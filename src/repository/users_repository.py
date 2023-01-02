from sqlalchemy.orm import Session
from .. import models, schemas


def create_user(db: Session, user: schemas.Users):
    new_user = models.Users(name=user.name, surname=user.surname, 
                username=user.username, age=user.age, gender=user.gender)
                
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(models.Users).all()


def get_user(id: int, db: Session):
    return db.query(models.Users).filter(models.Users.user_id == id).first()


def update_user(id: int, updated_user: schemas.Users, db: Session):
    
    update = db.query(models.Users).filter(models.Users.user_id == id).update(
        updated_user.dict(),synchronize_session=False)

    db.commit()
    return update

def delete_user(delete_user: schemas.Users, db: Session):
    db.delete(delete_user)
    db.commit()
    db.flush()
