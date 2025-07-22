from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from app import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------- USERS ----------

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).filter(models.User.email == email))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(models.User).filter(models.User.username == username))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# ---------- TASKS ----------

async def create_task(db: AsyncSession, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_tasks(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 20):
    result = await db.execute(
        select(models.Task).filter(models.Task.owner_id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int, user_id: int):
    result = await db.execute(
        select(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id)
    )
    return result.scalar_one_or_none()

async def delete_task(db: AsyncSession, task_id: int, user_id: int):
    task = await get_task(db, task_id, user_id)
    if task:
        await db.delete(task)
        await db.commit()
    return task

# ---------- NOTES ----------

async def create_note(db: AsyncSession, note: schemas.NoteCreate, user_id: int):
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    await db.commit()
    await db.refresh(db_note)
    return db_note

async def get_notes(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 20):
    result = await db.execute(
        select(models.Note).filter(models.Note.owner_id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def get_note(db: AsyncSession, note_id: int, user_id: int):
    result = await db.execute(
        select(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id)
    )
    return result.scalar_one_or_none()

async def delete_note(db: AsyncSession, note_id: int, user_id: int):
    note = await get_note(db, note_id, user_id)
    if note:
        await db.delete(note)
        await db.commit()
    return note
