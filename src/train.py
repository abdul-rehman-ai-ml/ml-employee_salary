# src/train.py
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# Ensure output dir exists
os.makedirs("model", exist_ok=True)

try:
    # Load data (minimal columns)
    df = pd.read_csv("data/employee_salary.csv", usecols=["Experience", "Education_Level", "Age", "Working_Hours", "Salary"])
    
    # Separate features and target
    X = df[["Experience", "Education_Level", "Age", "Working_Hours"]].values  # Use .values for efficiency
    y = df["Salary"].values

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Evaluate on training data (for sanity check)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))

    print(f"✅ Training complete | R²: {r2:.4f}, RMSE: {rmse:.2f}")

    # Save model and metrics
    joblib.dump(model, "model/model.pkl", compress=3)  # compress reduces .pkl size
    with open("model/metrics.txt", "w") as f:
        f.write(f"r2: {r2}\nrmse: {rmse}\n")

except Exception as e:
    print(f"❌ Training failed: {e}")
    raise SystemExit(1)