from fastapi import APIRouter
from ml.timetable_optimizer import solve_timetable

router = APIRouter(prefix="/timetable", tags=["timetable"])


@router.post("/optimize")
def optimize():
    return {"schedule": solve_timetable()}
