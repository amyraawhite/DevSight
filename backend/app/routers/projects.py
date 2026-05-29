from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..models import Project
from ..routers.auth import get_db
from ..schemas import ProjectCreate, ProjectUpdate, ProjectResponse

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("", response_model=list[ProjectResponse])
def get_projects(current_user=Depends(get_current_user),db: Session = Depends(get_db)):
    projects = db.query(Project).filter(
        Project.owner_id == current_user.id
    ).all()

    return projects

@router.post("", response_model=ProjectResponse)
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

@router.get("/{id}", response_model=ProjectResponse)
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

@router.patch("/{id}", response_model=ProjectResponse)
def update_project(id : int, project_update : ProjectUpdate, current_user=Depends(get_current_user), db : Session = Depends(get_db)): 
    existing_project = db.query(Project).filter(
        Project.id == id,
        Project.owner_id == current_user.id
    ).first()

    if not existing_project: 
        raise HTTPException(
            status_code=404,
            detail=f"No project with id : {id} exists."
        )
    
    if project_update.name is not None: 
        duplicate_project = db.query(Project).filter(
            Project.name == project_update.name,
            Project.owner_id == current_user.id,
            Project.id != id
        ).first()

        if duplicate_project: 
            raise HTTPException(
                status_code=400,
                detail=f"Project with name, {project_update.name}, alreay exists"
            )

        existing_project.name = project_update.name
    
    if project_update.description is not None:
        existing_project.description = project_update.description
    
    
    db.commit()
    db.refresh(existing_project)

    return existing_project



@router.delete("/{id}")
def delete_project(id : int, current_user=Depends(get_current_user), db : Session = Depends(get_db)): 
    existing_project = db.query(Project).filter(
        Project.id == id,
        Project.owner_id == current_user.id
    ).first()

    if not existing_project: 
        raise HTTPException(
            status_code=404,
            detail=f"No project with id : {id} exists."
        )
    
    db.delete(existing_project)
    db.commit()

    return {
        "message" : "Project deleted successfully"
    }






