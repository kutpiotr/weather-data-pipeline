import requests

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

print("\nAvailable top-level keys:")
print(data.keys())

print("\nDaily data:")
print(data["daily"])