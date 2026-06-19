# preprocess

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

def duration_to_min(x):
    hours = 0
    minutes = 0

    if pd.isna(x):
        return None

    x = x.strip()

    if 'h' in x:
        hours = int(x.split('h')[0])

    if 'm' in x:
        if 'h' in x:
            minutes = int(
                x.split('h')[1].replace('m', '').strip()
            )
        else:
            minutes = int(
                x.replace('m', '').strip()
            )

    return hours * 60 + minutes



def duration_to_min_convert(X):
  X = X.copy()

  X['Duration'] = X['Duration'].apply(duration_to_min)

  return X


class DropColumns(BaseEstimator, TransformerMixin):

    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(columns=self.columns)

def extract_date_of_journey(X):
  X = X.copy()

  X["Date_of_Journey"] = pd.to_datetime(
        X["Date_of_Journey"],
        format="%d/%m/%Y",
        errors="coerce"
    )

  X['Journey_day'] = X['Date_of_Journey'].dt.day
  X['Journey_month'] = X['Date_of_Journey'].dt.month
  X['Day_of_week'] = X['Date_of_Journey'].dt.dayofweek
  X["Is_weekend"] = (X["Day_of_week"] >= 5).astype(int)

  return X.drop(columns=['Date_of_Journey'])

def time_of_day(hour):
  if hour < 5:          # 0-4 -> Late night
    return 'Late night'
  elif hour < 12:       # 5-11 -> Morning
    return 'Morning'
  elif hour < 17:       # 12-16 -> Afternoon
    return 'Afternoon'
  elif hour < 21:       # 17-20 -> Evening
    return 'Evening'
  else:
    return 'Night'      # 21-23 -> Night

def extract_departure_time(X):
  X = X.copy()

  X["Dep_Time"] = pd.to_datetime(
        X["Dep_Time"],
        format="%H:%M",
        errors="coerce"
    )

  X['Dep_hour'] = X['Dep_Time'].dt.hour
  X['Time_of_day'] = X['Dep_hour'].apply(time_of_day)

  return X.drop(columns=['Dep_Time'])


def extract_arrival_time(X):
    X = X.copy()

    X["Arrival_next_day"] = (
        X["Arrival_Time"].str.contains(" ", regex=False)
    ).astype(int)

    time_part = X["Arrival_Time"].str.split().str[0]

    arrival_dt = pd.to_datetime(
        time_part,
        format="%H:%M",
        errors="coerce"
    )

    X["Arr_hour"] = arrival_dt.dt.hour

    return X.drop(columns=["Arrival_Time"])

def clean_values(X):
  X = X.copy()

  X['Source'] = X['Source'].replace({'Banglore':'Bangalore', 'Delhi':'New Delhi'})
  X['Destination'] = X['Destination'].replace({'Banglore':'Bangalore', 'Delhi':'New Delhi'})
  X['Additional_Info'] = X['Additional_Info'].replace({'No Info':'No info'})

  return X

def transform_total_stops(X):
  X = X.copy()

  stop_mapping = {
        "non-stop": 0,
        "1 stop": 1,
        "2 stops": 2,
        "3 stops": 3,
        "4 stops": 4
  }

  X["Total_Stops"] = X["Total_Stops"].map(stop_mapping)

  return X


  


