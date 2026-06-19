from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_fare

app = FastAPI()

class FlightFareRequest(BaseModel):
    Airline: str
    Date_of_Journey: str
    Source: str
    Destination: str
    Route: str
    Dep_Time: str
    Arrival_Time: str
    Duration: str
    Total_Stops: str
    Additional_Info: str

@app.get("/")
def home():
    return {"message": "Welcome to the Flight Fare Prediction API!"}

@app.post("/predict")
def predict(data: FlightFareRequest):
    fare = predict_fare(data.model_dump())

    return {"predicted_fare": fare}

