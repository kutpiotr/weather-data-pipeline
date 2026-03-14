import sqlite3
from pathlib import Path

import pandas as pd
import requests

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"

BASE_URL="https://api.open-meteo.com/v1/forecast"

CITY_NAME="Rzeszow"

params={
"latitude":50.0413,
"longitude":21.9990,
"daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
"timezone":"Europe/Warsaw"
}

def fetch_weather_data():
    response=requests.get(BASE_URL,params=params,timeout=10)
    response.raise_for_status()
    data=response.json()

    daily_data=data["daily"]

    df=pd.DataFrame({
    "city":CITY_NAME,
    "date":daily_data["time"],
    "temperature_max":daily_data["temperature_2m_max"],
    "temperature_min":daily_data["temperature_2m_min"],
    "precipitation_sum":daily_data["precipitation_sum"]
    })

    df["date"]=pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    return df

def load_to_sqlite(df):
    with sqlite3.connect(DB_PATH) as connection:
        df.to_sql("weather_data",connection,if_exists="append",index=False)

def main():
    df=fetch_weather_data()

    print("Downloaded data:")
    print(df)

    load_to_sqlite(df)

    print(f"\nLoaded {len(df)} rows into database: {DB_PATH}")

if __name__=="__main__":
    main()