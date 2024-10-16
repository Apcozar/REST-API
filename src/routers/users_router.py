from typing import List
from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.session import get_session
from ..schemas.users_schemas import UserCreate, UserBase, UserOut
from ..repository import users_repository
from ..core.security import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, session: Session = Depends(get_session), 
    cur_user: int = Depends(get_current_user)):

    existing_user = users_repository.get_user_by_username(user.username, session)

    if not cur_user or not cur_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin user")

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"{user.username} username already taken")

    existing_email = users_repository.get_user_by_email(user.email, session)

    if existing_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"{user.email} email already taken")

    new_user = users_repository.create_user(user, session)
    return new_user


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserOut])
def get_users(session: Session = Depends(get_session), cur_user: int = Depends(get_current_user)):
    users = users_repository.get_users(session)
    return users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user(id: int, session: Session = Depends(get_session), cur_user: int = Depends(get_current_user)):
    user = users_repository.get_user(id, session)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"user with id: {id} does not exist")

    return user


@router.patch("/{id}")
def update_user(id: int, updated_user: UserBase, session: Session = Depends(get_session), cur_user: int = Depends(get_current_user)):

    existing_user = users_repository.get_user(id, session)

    if not existing_user or not cur_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"user with id: {id} does not exist")

    if existing_user.user_id != cur_user.user_id and not cur_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You cannot update this user")

    existing_username = users_repository.get_user_by_username(updated_user.username, session)

    if existing_username:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"{existing_username.username} username is already taken")


    updated_data = updated_user.dict(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_user, key, value)

    users_repository.update_user(id, existing_user, session)  
         
    return {"msg": "User successfully updated"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: Session = Depends(get_session), cur_user: int = Depends(get_current_user)):
    existing_user = users_repository.get_user(id, session)

    if not existing_user or not cur_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"user with id: {id} does not exist")

    if existing_user.user_id != cur_user.user_id and not cur_user.is_admin or existing_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You cannot delete this user")

    users_repository.delete_user(id, session)

    return Response(status_code=status.HTTP_204_NO_CONTENT)