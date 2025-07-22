from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import crud, schemas
from app.database import get_db
from app.auth_helper import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=schemas.TaskOut)
async def create_task(
    task: schemas.TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return await crud.create_task(db, task, user_id=current_user.id)

@router.get("/", response_model=List[schemas.TaskOut])
async def read_tasks(
    skip: int = 0, limit: int = 20,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return await crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit)

@router.delete("/{task_id}", response_model=schemas.TaskOut)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    task = await crud.delete_task(db, task_id, user_id=current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
