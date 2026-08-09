from fastapi import APIRouter
from pydantic import BaseModel

from app.graph import graph

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentRunRequest(BaseModel):
    student_id: int
    query: str
    risk_score: float = 0.4


@router.post("/run")
def run_agents(payload: AgentRunRequest):
    result = graph.invoke(payload.model_dump())
    return result
