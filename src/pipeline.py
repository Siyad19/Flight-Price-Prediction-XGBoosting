# pipeline.py
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from src.preprocess import *

def create_pipeline(model):

    clean_transformer = FunctionTransformer(
        clean_values,
        validate=False
    )

    date_of_journey_transformer = FunctionTransformer(
        extract_date_of_journey,
        validate=False
    )

    departure_transformer = FunctionTransformer(
        extract_departure_time,
        validate=False
    )

    arrival_transformer = FunctionTransformer(
        extract_arrival_time,
        validate=False
    )

    duration_transformer = FunctionTransformer(
        duration_to_min_convert,
        validate=False
    )

    total_stops_transformer = FunctionTransformer(
        transform_total_stops,
        validate=False
    )

    numeric_cols = [
        "Journey_day",
        "Journey_month",
        "Day_of_week",
        "Is_weekend",
        "Dep_hour",
        "Arr_hour",
        "Arrival_next_day",
        "Duration",
        "Total_Stops"
    ]

    categorical_cols = [
        "Airline",
        "Source",
        "Destination",
        "Additional_Info",
        "Time_of_day"
    ]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, numeric_cols),
        ("cat", categorical_pipeline, categorical_cols)
    ], remainder="drop")

    pipeline = Pipeline([
        ("clean_values", clean_transformer),
        ("date_of_journey", date_of_journey_transformer),
        ("departure_time", departure_transformer),
        ("arrival_time", arrival_transformer),
        ("duration", duration_transformer),
        ("total_stops", total_stops_transformer),
        ("drop_cols", DropColumns(["Route"])),
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline