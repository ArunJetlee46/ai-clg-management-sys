import numpy as np
import pandas as pd


def generate(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    attendance = rng.uniform(40, 100, n)
    gpa = rng.uniform(4, 10, n)
    arrears = rng.integers(0, 8, n)
    engagement = rng.uniform(0, 1, n)
    dropout = ((attendance < 65).astype(int) + (gpa < 6).astype(int) + (arrears > 3).astype(int) + (engagement < 0.35).astype(int) >= 2).astype(int)
    placement = ((gpa > 7).astype(int) + (arrears < 2).astype(int) + (engagement > 0.5).astype(int) >= 2).astype(int)
    return pd.DataFrame({
        "attendance_pct": attendance,
        "gpa": gpa,
        "arrears": arrears,
        "engagement_score": engagement,
        "dropout": dropout,
        "placement": placement,
    })
