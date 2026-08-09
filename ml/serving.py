from pathlib import Path
import joblib
import numpy as np

MODEL_PATH = Path("ml/models/dropout_model.joblib")


def _load_model():
    if not MODEL_PATH.exists():
        from ml.train_models import train_and_save
        train_and_save(str(MODEL_PATH.parent))
    return joblib.load(MODEL_PATH)


def predict_dropout(features: dict) -> float:
    model = _load_model()
    x = np.array([[features["attendance_pct"], features["gpa"], features["arrears"], features["engagement_score"]]])
    return model.predict_proba(x)[0][1]
