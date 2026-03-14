import requests

BASE_URL="https://api.open-meteo.com/v1/forecast"

def fetch_weather_data(latitude,longitude,timezone="Europe/Warsaw"):
    params={
    "latitude":latitude,
    "longitude":longitude,
    "daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone":timezone
    }

    response=requests.get(BASE_URL,params=params,timeout=10)
    response.raise_for_status()

    return response.json()