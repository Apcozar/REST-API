from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..schemas.users import UserCreate
from ..repository import users_repository

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = users_repository.create_user(db, user)
    return {"data": new_user}


@router.get("/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = users_repository.get_users(db)
    return {"data": users}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user = users_repository.get_user(id, db)

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    return {"data": user}


@router.post("/{id}")
def update_user(id: int, updated_user: UserCreate, db: Session = Depends(get_db)):

    updated = users_repository.update_user(id, updated_user, db)  

    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")
         
    return updated_user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = users_repository.get_user(id, db)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    users_repository.delete_user(id, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)