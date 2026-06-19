# train.py

import joblib
import numpy as np
import pandas as pd

from xgboost import XGBRegressor

from sklearn.compose import TransformedTargetRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.pipeline import create_pipeline

def main():

    # Load data
    df = pd.read_excel("data/Flight_Fare.xlsx")

    # Features and target
    X = df.drop(columns=["Price"])
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Your tuned XGBoost model
    xgb_model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.2,
        random_state=42
    )

    model = TransformedTargetRegressor(
        regressor=xgb_model,
        func=np.log1p,
        inverse_func=np.expm1
    )

    # Create complete pipeline
    pipeline = create_pipeline(model)

    # Train
    pipeline.fit(X_train, y_train)

    # Predict
    y_pred = pipeline.predict(X_test)

    # Evaluate
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: {rmse:.2f}")

    print(f"R² Score: {r2_score(y_test, y_pred):.4f}")

    # Save pipeline
    joblib.dump(
        pipeline,
        "model/flight_price_model.joblib"
    )

    print("\nPipeline saved successfully!")


if __name__ == "__main__":
    main()