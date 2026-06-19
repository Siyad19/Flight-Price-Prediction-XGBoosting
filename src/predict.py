# predict.py

import joblib
import pandas as pd

model_path = "model/flight_price_pipeline.joblib"

pipeline = joblib.load(model_path)

def predict_fare(input_data: dict) -> float:
    df = pd.DataFrame([input_data])

    prediction = pipeline.predict(df)[0]

    return round(float(prediction), 2)

if __name__ == "__main__":
    sample = {
        "Airline": "IndiGo",
        "Date_of_Journey": "24/03/2019",
        "Source": "Delhi",
        "Destination": "Cochin",
        "Route": "Delhi → Cochin",
        "Dep_Time": "22:20",
        "Arrival_Time": "01:10",
        "Duration": "2h 50m",
        "Total_Stops": "non-stop",
        "Additional_Info": "No info"
    }

    print(predict_fare(sample))