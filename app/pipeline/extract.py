import requests

from app.settings import API_TIMEOUT,TIMEZONE

BASE_URL="https://api.open-meteo.com/v1/forecast"

def fetch_weather_data(latitude,longitude):
    params={
    "latitude":latitude,
    "longitude":longitude,
    "daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone":TIMEZONE
    }

    response=requests.get(BASE_URL,params=params,timeout=API_TIMEOUT)
    response.raise_for_status()

    return response.json()