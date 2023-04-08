from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from database.engine import get_engine, get_session, create_table

from models.user_model import  User, UserCreate, UserRead, UserUpdate
from models.board_model import Board, BoardCreate, BoardRead, BoardUpdate
from models.note_model import Note, NoteCreate, NoteRead, NoteUpdate
from models.link import UserBoardLink


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_table()


@app.post('/user/', response_model=UserRead)
def create_user(
    *, 
    session: Session = Depends(get_session), 
    user: UserCreate
):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get('/user/', response_model=List[UserRead])
def read_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.get('/user/{user_id}', response_model=UserRead)
def read_user(
    *, 
    session: Session = Depends(get_session), 
    user_id: int
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.patch('/user/{user_id}', response_model=UserRead)
def update_user(
    *, 
    session: Session = Depends(get_session), 
    user_id: int,
    user: UserUpdate
):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.delete('/user/{user_id}')
def delete_user(
    *, 
    session: Session = Depends(get_session), 
    user_id: int
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}


# ------------------------------------------------------------------------------------------------------------------------


@app.post('/board/', response_model=BoardRead)
def create_board(
    *, 
    session: Session = Depends(get_session), 
    board: BoardCreate
):
    db_board = Board.from_orm(board)
    session.add(db_board)
    session.commit()
    session.refresh(db_board)
    return db_board


@app.get('/board/', response_model=List[BoardRead])
def read_boards(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    boards = session.exec(select(Board).offset(offset).limit(limit)).all()
    return boards


@app.get('/board/{board_id}', response_model=BoardRead)
def read_board(
    *, 
    session: Session = Depends(get_session), 
    board_id: int
):
    board = session.get(Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@app.patch('/board/{board_id}', response_model=BoardRead)
def update_board(
    *, 
    session: Session = Depends(get_session), 
    board_id: int,
    board: BoardUpdate
):
    db_board = session.get(Board, board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    board_data = board.dict(exclude_unset=True)
    for key, value in board_data.items():
        setattr(db_board, key, value)
    session.add(db_board)
    session.commit()
    session.refresh(db_board)
    return db_board


@app.delete('/board/{board_id}')
def delete_board(
    *, 
    session: Session = Depends(get_session), 
    board_id: int
):
    board = session.get(Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    session.delete(board)
    session.commit()
    return {"ok": True}


# ------------------------------------------------------------------------------------------------------------------------


@app.post('/note/', response_model=NoteRead)
def create_note(
    *, 
    session: Session = Depends(get_session), 
    note: NoteCreate
):
    db_note = Note.from_orm(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


@app.get('/note/', response_model=List[NoteRead])
def read_notes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    notes = session.exec(select(Note).offset(offset).limit(limit)).all()
    return notes


@app.get('/note/{note_id}', response_model=NoteRead)
def read_note(
    *, 
    session: Session = Depends(get_session), 
    note_id: int
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.patch('/note/{note_id}', response_model=NoteRead)
def update_note(
    *, 
    session: Session = Depends(get_session), 
    note_id: int,
    note: NoteUpdate
):
    db_note = session.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_data = note.dict(exclude_unset=True)
    for key, value in note_data.items():
        setattr(db_note, key, value)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


@app.delete('/note/{note_id}')
def delete_note(
    *, 
    session: Session = Depends(get_session), 
    note_id: int
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"ok": True}