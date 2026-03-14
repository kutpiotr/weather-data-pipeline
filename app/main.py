import requests
import pandas as pd

BASE_URL="https://api.open-meteo.com/v1/forecast"

params={
"latitude":50.0413,
"longitude":21.9990,
"daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
"timezone":"Europe/Warsaw"
}

response=requests.get(BASE_URL,params=params,timeout=10)
print("Status code:",response.status_code)

response.raise_for_status()

data=response.json()
daily_data=data["daily"]

df=pd.DataFrame({
"date":daily_data["time"],
"temperature_max":daily_data["temperature_2m_max"],
"temperature_min":daily_data["temperature_2m_min"],
"precipitation_sum":daily_data["precipitation_sum"]
})

df["date"]=pd.to_datetime(df["date"])

print("\nDataFrame preview:")
print(df)

print("\nDataFrame info:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())