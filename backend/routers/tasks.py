from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jose import jwt

from database import SessionLocal
from models import User, Task
from schemas import TaskCreate
from auth import SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token=Depends(security)
):

    payload = jwt.decode(
        token.credentials,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload["sub"]


@router.post("/")
def create_task(
    task: TaskCreate,
    username=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=user.id
    )

    db.add(new_task)
    db.commit()

    return {
        "message": "Task Created"
    }


@router.get("/")
def get_tasks(
    username=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    return db.query(Task).filter(
        Task.owner_id == user.id
    ).all()


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskCreate,
    username=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == user.id
    ).first()

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db_task.title = task.title
    db_task.description = task.description

    db.commit()

    return {
        "message": "Task Updated"
    }


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    username=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == user.id
    ).first()

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(db_task)
    db.commit()

    return {
        "message": "Task Deleted"
    }