from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.board_model import Board


class NoteBase(SQLModel):
    title: str = Field(index=True)
    # privat: bool
    content: str


class Note(NoteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # board_id: Optional[int] = Field(default=None, foreign_key='board.id')


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int


class NoteUpdate(SQLModel):
    id: Optional[int] = None
    title: Optional[str] = None
    # privat: Optional[bool] = None
    content: str

