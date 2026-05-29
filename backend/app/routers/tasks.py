from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..models import Task, Project
from ..database import get_db

from ..schemas import TaskResponse, TaskUpdate


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id : int, current_user=Depends(get_current_user), db : Session=Depends(get_db)): 
    existing_task = db.query(Task).join(Project).filter(
        Task.id == task_id,
        Project.owner_id == current_user.id
    ).first()

    if not existing_task: 
        raise HTTPException(
            status_code=404,
            detail=f"Task with id, {task_id}, does noy exist"
        )

    return existing_task

@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_id : int, task_update : TaskUpdate, current_user=Depends(get_current_user), db : Session=Depends(get_db)): 
    existing_task = db.query(Task).join(Project).filter(
        Task.id == task_id,
        Project.owner_id == current_user.id
    ).first()

    if not existing_task: 
        raise HTTPException(
            status_code=404,
            detail=f"Task with id, {task_id}, does not exist"
        )


    if task_update.title is not None: 
        existing_title = db.query(Task).filter(
            Task.project_id == existing_task.project_id,
            Task.title == task_update.title,
            Task.id != task_id
        ).first()

        if existing_title: 
            raise HTTPException(
                status_code=400,
                detail=f'Task with title, "{task_update.title}", already exists'
            )
        
        existing_task.title = task_update.title

    if task_update.description is not None:
        existing_task.description = task_update.description

    if task_update.priority is not None:
        existing_task.priority = task_update.priority

    if task_update.status is not None:
        existing_task.status = task_update.status

    db.commit()
    db.refresh(existing_task)

    return existing_task

@router.delete("/{task_id}")
def delete_task(task_id : int, current_user = Depends(get_current_user), db : Session=Depends(get_db)): 
    existing_task = db.query(Task).join(Project).filter(
        Project.owner_id == current_user.id,
        Task.id == task_id
    ).first()

    if not existing_task: 
        raise HTTPException(
            status_code=404,
            detail=f"Task with id, {task_id}, does noy exist"
        )
    
    db.delete(existing_task)
    db.commit()

    return {
        "message" : "Task deleted successfully"
    }