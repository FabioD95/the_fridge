from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from database.engine import get_engine, get_session, create_table

from models.board_model import Board, BoardCreate, BoardRead, BoardUpdate


router = APIRouter()


@router.post('/board/', response_model=BoardRead)
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


@router.get('/board/', response_model=List[BoardRead])
def read_boards(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    boards = session.exec(select(Board).offset(offset).limit(limit)).all()
    return boards


@router.get('/board/{board_id}', response_model=BoardRead)
def read_board(
    *, 
    session: Session = Depends(get_session), 
    board_id: int
):
    board = session.get(Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@router.patch('/board/{board_id}', response_model=BoardRead)
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


@router.delete('/board/{board_id}')
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
