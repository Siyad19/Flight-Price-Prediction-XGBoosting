# Flight Fare Prediction System

An end-to-end Machine Learning project that predicts flight ticket prices based on airline, journey date, source, destination, departure time, arrival time, duration, number of stops, and additional flight information.

The project demonstrates a complete AI/ML workflow from data preprocessing and feature engineering to model deployment using FastAPI.

---

## Features

* Automated data preprocessing using Scikit-learn pipelines
* Custom feature engineering with reusable transformers
* Missing value handling with SimpleImputer
* Categorical feature encoding using OneHotEncoder
* Model training using XGBoost Regressor
* Target variable transformation using log transformation
* Model serialization using Joblib
* REST API development using FastAPI

---

## Model Performance

| Metric   | Score   |
| -------- | ------- |
| MAE      | 694.49  |
| RMSE     | 1387.97 |
| R² Score | 0.9090  |

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* FastAPI
* Pydantic
* Joblib
* Uvicorn

---

## Project Structure

```text
flight-fare-prediction/
│
├── data/
│   └── Flight_Fare.xlsx/
│   
│
├── models/
│   └── flight_price_pipeline.joblib
│
├── notebooks/
│   └── flight_fare_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── pipeline.py
│   ├── train.py
│   └── predict.py
│   
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flight-fare-prediction.git
cd flight-fare-prediction
```

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n flight_price python=3.12
conda activate flight_price
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

Place the dataset inside the `data/` directory.

Run:

```bash
python -m src.train
```

After successful training, the model pipeline will be saved as:

```text
models/flight_price_pipeline.joblib
```

---

## Run Predictions Locally

Test the prediction module:

```bash
python -m src.predict
```

---

## Run the FastAPI Application

Start the API server:

```bash
uvicorn src.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

### POST `/predict`

Request body:

```json
{
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
```

Example response:

```json
{
  "predicted_fare": 5470.19
}
```

---

## Machine Learning Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Preprocessing Pipeline
   ↓
Model Training (XGBoost)
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
FastAPI Deployment
```

---

## Feature Engineering

The following custom features are created during preprocessing:

* Journey day
* Journey month
* Day of week
* Weekend indicator
* Departure hour
* Time of day
* Arrival hour
* Arrival next day flag
* Duration in minutes
* Total stops mapping

---

## Future Improvements

* Docker support
* Cloud deployment
* CI/CD pipeline
* Streamlit frontend

---

