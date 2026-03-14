import pandas as pd

def transform_weather_data(raw_data,city_name):
    daily_data=raw_data["daily"]

    df=pd.DataFrame({
    "city":city_name,
    "date":daily_data["time"],
    "temperature_max":daily_data["temperature_2m_max"],
    "temperature_min":daily_data["temperature_2m_min"],
    "precipitation_sum":daily_data["precipitation_sum"]
    })

    df["date"]=pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    return df