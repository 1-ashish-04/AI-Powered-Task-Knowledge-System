from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user

from app.models.user import User
from app.models.task import Task

from app.schemas.task import TaskCreate, TaskResponse
from app.schemas.task import TaskUpdate
from datetime import datetime

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    assigned_user = db.query(User).filter(
        User.id == task.assigned_to
    ).first()

    if not assigned_user:
        raise HTTPException(
            status_code=404,
            detail="Assigned user not found."
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        deadline=task.deadline,
        assigned_to=task.assigned_to,
        created_by=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Task).all()

@router.get(
    "/my",
    response_model=list[TaskResponse]
)
def get_my_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Task).filter(
        Task.assigned_to == current_user.id
    ).all()

@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    return task

@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    update_data = updated_task.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully."
    }

@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse
)
def complete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    task.status = "Completed"
    task.completed_at = datetime.utcnow()

    db.commit()
    db.refresh(task)

    return task