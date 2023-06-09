from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.board_model import Board


class NoteBase(SQLModel):
    title: str = Field(index=True)
    private: bool
    content: str
    board_id: int = Field(default=None, foreign_key='board.id')


class Note(NoteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int


class NoteUpdate(SQLModel):
    id: Optional[int] = None
    title: Optional[str] = None
    privat: Optional[bool] = None
    content: Optional[str] = None

