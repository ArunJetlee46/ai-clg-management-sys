from fastapi import APIRouter
from pydantic import BaseModel

from ml.serving import predict_dropout

router = APIRouter(prefix="/ml", tags=["ml"])


class DropoutPredictRequest(BaseModel):
    attendance_pct: float
    gpa: float
    arrears: int
    engagement_score: float


@router.post("/dropout/predict")
def predict(payload: DropoutPredictRequest):
    score = float(predict_dropout(payload.model_dump()))
    return {"risk_score": score}
