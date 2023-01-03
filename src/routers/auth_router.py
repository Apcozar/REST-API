from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..db.session import get_session
from ..schemas.users_schemas import Token
from ..repository import users_repository
from ..core import security

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=Token)
def login(user_login: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    existing_user = users_repository.get_user_by_email(
                        user_login.username, session)

    if not existing_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail="There's any user with email")

    if not security.verify(user_login.password, existing_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password")

    token = security.create_access_token(data= {"user_id": existing_user.user_id})

    return {"access_token": token, "token_type": "bearer"}