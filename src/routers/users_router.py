from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.session import get_session
from ..schemas.users import UserCreate, UserBase
from ..repository import users_repository

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    new_user = users_repository.create_user(session, user)
    return {"data": new_user}


@router.get("/", status_code=status.HTTP_200_OK)
def get_users(session: Session = Depends(get_session)):
    users = users_repository.get_users(session)
    return {"data": users}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, session: Session = Depends(get_session)):
    user = users_repository.get_user(id, session)

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    return {"data": user}


@router.patch("/{id}")
def update_user(id: int, updated_user: UserBase, session: Session = Depends(get_session)):

    existing_user = users_repository.get_user(id, session)

    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    updated_data = updated_user.dict(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_user, key, value)

    users_repository.update_user(id, existing_user, session)  
         
    return existing_user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: Session = Depends(get_session)):
    user = users_repository.get_user(id, session)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    users_repository.delete_user(id, session)

    return Response(status_code=status.HTTP_204_NO_CONTENT)