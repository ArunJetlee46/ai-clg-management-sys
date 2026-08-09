from pathlib import Path
import joblib
import shap
from lime.lime_tabular import LimeTabularExplainer

from ml.synthetic_data import generate


def generate_explanations(model_path: str = "ml/models/dropout_model.joblib"):
    df = generate(200)
    X = df[["attendance_pct", "gpa", "arrears", "engagement_score"]]
    model = joblib.load(model_path)

    clf = model.named_steps["clf"]
    transformed = model.named_steps["scaler"].transform(X)
    shap_explainer = shap.TreeExplainer(clf)
    shap_values = shap_explainer.shap_values(transformed[:20])

    lime_exp = LimeTabularExplainer(transformed, feature_names=list(X.columns), class_names=["safe","risk"], discretize_continuous=True)
    lime_instance = lime_exp.explain_instance(transformed[0], clf.predict_proba)

    out = Path("ml/explanations")
    out.mkdir(parents=True, exist_ok=True)
    lime_instance.save_to_file(str(out / "lime_example.html"))
    return {"shap_samples": len(shap_values[0]), "lime_file": str(out / "lime_example.html")}
