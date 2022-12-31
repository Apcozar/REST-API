from sqlalchemy.orm import Session
from .. import models, schemas


def create_user(db: Session, user: schemas.InUser):
    new_user = models.User(name=user.name, surname=user.surname, description=user.description)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(id: int, db: Session):
    return db.query(models.User).filter(models.User.id == id).first()


def update_user(id: int, updated_user: schemas.InUser, db: Session):
    
    update = db.query(models.User).filter(models.User.id == id).update(
        updated_user.dict(),synchronize_session=False)

    db.commit()
    return update

def delete_user(delete_user: schemas.InUser, db: Session):
    db.delete(delete_user)
    db.commit()
    db.flush()
