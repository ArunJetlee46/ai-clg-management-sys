from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import mlflow

from ml.synthetic_data import generate


def train_and_save(out_dir: str = "ml/models"):
    df = generate()
    X = df[["attendance_pct", "gpa", "arrears", "engagement_score"]]
    y_dropout = df["dropout"]

    X_train, X_test, y_train, y_test = train_test_split(X, y_dropout, test_size=0.2, random_state=42)
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=150, random_state=42)),
    ])
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    mlflow.set_experiment("aegis-campus")
    with mlflow.start_run(run_name="dropout-model"):
        mlflow.log_metric("accuracy", score)

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, Path(out_dir) / "dropout_model.joblib")
    return score


if __name__ == "__main__":
    print({"accuracy": train_and_save()})
