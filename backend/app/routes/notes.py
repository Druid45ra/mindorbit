from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import crud, schemas
from app.database import get_db
from app.auth_helper import get_current_user

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=schemas.NoteOut)
async def create_note(
    note: schemas.NoteCreate,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return await crud.create_note(db, note, user_id=current_user.id)

@router.get("/", response_model=List[schemas.NoteOut])
async def read_notes(
    skip: int = 0, limit: int = 20,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return await crud.get_notes(db, user_id=current_user.id, skip=skip, limit=limit)

@router.delete("/{note_id}", response_model=schemas.NoteOut)
async def delete_note(
    note_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    note = await crud.delete_note(db, note_id, user_id=current_user.id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
