from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..models import Project
from ..routers.auth import get_db
from ..schemas import ProjectCreate

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("")
def get_projects(current_user=Depends(get_current_user),db: Session = Depends(get_db)):
    projects = db.query(Project).filter(
        Project.owner_id == current_user.id
    ).all()

    return projects

@router.post("")
def post_project(project: ProjectCreate, current_user=Depends(get_current_user), db: Session = Depends(get_db)):

    existing_project = db.query(Project).filter(
        current_user.id == Project.owner_id,
        Project.name == project.name
    ).first()

    if existing_project:
        raise HTTPException(
            status_code=400,
            detail="Project already exists."
        )

    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=current_user.id
    )
    
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@router.get("/{id}")
def get_project_by_id(id : int, current_user=Depends(get_current_user),db: Session = Depends(get_db)):
    project = db.query(Project).filter(
        Project.id == id,
        Project.owner_id == current_user.id
    ).first()

    if not project: 
        raise HTTPException(
            status_code=404,
            detail=f"No project with id : {id} exists."
        )
    
    return project


