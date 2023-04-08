from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from models.board_model import Board
from models.link import UserBoardLink


class UserBase(SQLModel):
    name: str = Field(index=True)
    email: str
    password: str


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # board: List['Board'] = Relationship(back_populates= 'boards', link_model=UserBoardLink)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str] = None
