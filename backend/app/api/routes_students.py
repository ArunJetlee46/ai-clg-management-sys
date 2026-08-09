from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.deps import require_roles
from app.models import Student
from app.schemas import StudentCreate, StudentOut

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentOut)
def create_student(payload: StudentCreate, db: Session = Depends(get_db), _=Depends(require_roles("admin", "faculty"))):
    obj = Student(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db), _=Depends(require_roles("admin", "faculty", "student"))):
    return db.query(Student).all()
