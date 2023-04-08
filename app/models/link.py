from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class UserBoardLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    board_id: Optional[int] = Field(default=None, foreign_key="board.id", primary_key=True)