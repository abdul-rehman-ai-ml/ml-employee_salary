# tests/test_model.py
import joblib
import pandas as pd

def test_model_r2():
    model = joblib.load("model/model.pkl")
    df = pd.read_csv("data/employee_salary.csv")
    X = df[["Experience", "Education_Level", "Age", "Working_Hours"]]
    y = df["Salary"]
    r2 = model.score(X, y)
    assert r2 > 0.95, f"R² too low: {r2:.4f}"
    print(f"✅ R² = {r2:.4f} — model is strong!")