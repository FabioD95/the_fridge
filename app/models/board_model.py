from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.user_model import User
from models.link import UserBoardLink


class BoardBase(SQLModel):
    title: str = Field(index=True)
    privat: bool


class Board(BoardBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # user: List['User'] = Relationship(back_populates= 'users', link_model=UserBoardLink)


class BoardCreate(BoardBase):
    pass


class BoardRead(BoardBase):
    id: int


class BoardUpdate(SQLModel):
    id: Optional[int] = None
    title: Optional[str] = None
    privat: Optional[bool] = None
