from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from database.engine import get_engine, get_session, create_table

from models.user_model import  User, UserCreate, UserRead, UserUpdate


router = APIRouter()


@router.post('/', response_model=UserRead)
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


@router.get('/', response_model=List[UserRead])
def read_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@router.get('/{user_id}', response_model=UserRead)
def read_user(
    *, 
    session: Session = Depends(get_session), 
    user_id: int
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch('/{user_id}', response_model=UserRead)
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


@router.delete('/{user_id}')
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