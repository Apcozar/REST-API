from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from ..schemas.users_schemas import TokenData
from ..db.session import get_session
from ..models.users import Users

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash(pwd: str):
    return pwd_context.hash(pwd)


def verify(pwd, hashed_pwd):
    return pwd_context.verify(pwd, hashed_pwd)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_access_token(token: str, exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")

        if not user_id:
            raise exception
    
        token_data = TokenData(id=user_id)

    except JWTError as e:
        print(e)
        raise exception
     
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail=f"Coudl not validate credentials", 
                    headers={"WWW-Authenticate": "Bearer"})
   
    token = verify_access_token(token, exception)
    cur_user = session.query(Users).filter(Users.user_id == token.id).first()
    
    return cur_user

