from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .base import Base


class Friendships(Base):
    __tablename__ = "friendships"

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    friend_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    creationTime = Column(TIMESTAMP(timezone=True), nullable=False, 
                    server_default=text("now()"))