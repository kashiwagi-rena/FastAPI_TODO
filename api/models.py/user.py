import datetime
from sqlalchemy import Column, Integer, String, DateTime
from typing import Optional


from settings.database import Base
from pydantic import BaseModel

class UserOrm(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    deleted_at = Column(DateTime, nullable=True)

class User(BaseModel):
    id = int
    name = str
    email = str
    created_at = datetime.datetime
    updated_at = datetime.datetime
    deleted_at = Optional[datetime.datetime]

    class Config:
        orm_mode = True