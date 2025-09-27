# src/train.py
import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

os.makedirs("model", exist_ok=True)

# Load data
df = pd.read_csv("data/employee_salary.csv")
X = df[["Experience", "Education_Level", "Age", "Working_Hours"]]
y = df["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Evaluate
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"R²: {r2:.4f}, RMSE: {rmse:.2f}")

# Save
joblib.dump(model, "model/model.pkl")
with open("model/metrics.txt", "w") as f:
    f.write(f"r2: {r2}\nrmse: {rmse}\n")

print("✅ Model trained and saved!")