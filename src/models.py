from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


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


class Friendships(Base):
    __tablename__ = "friendships"

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    friend_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    creationTime = Column(TIMESTAMP(timezone=True), nullable=False, 
                    server_default=text("now()"))
                    