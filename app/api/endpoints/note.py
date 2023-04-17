from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from database.engine import get_engine, get_session, create_table

from models.note_model import Note, NoteCreate, NoteRead, NoteUpdate


router = APIRouter()


@router.post('/note/', response_model=NoteRead)
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


@router.get('/note/', response_model=List[NoteRead])
def read_notes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    notes = session.exec(select(Note).offset(offset).limit(limit)).all()
    return notes


@router.get('/note/{note_id}', response_model=NoteRead)
def read_note(
    *, 
    session: Session = Depends(get_session), 
    note_id: int
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.patch('/note/{note_id}', response_model=NoteRead)
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


@router.delete('/note/{note_id}')
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