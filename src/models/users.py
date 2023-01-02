from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=40), nullable=False)
    surname = Column(String(length=40), nullable=False)
    username = Column(String(length=20), unique=True, nullable=False)
    creationTime = Column(TIMESTAMP(timezone=True), nullable=False, 
                    server_default=text("now()"))
    age = Column(Integer, nullable=False)
    gender = Column(String(length=20), nullable=False)