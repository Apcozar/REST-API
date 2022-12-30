from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.InUser, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, surname=user.surname, description=user.description)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user}


@router.get("/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {"data": users}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    return {"data": user}


@router.post("/{id}")
def update_user(id: int, updated_user: schemas.InUser, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    user_query.update(updated_user.dict(), synchronize_session=False)

    db.commit()

    return {"data": "succesful"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    user_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)