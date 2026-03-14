import pandas as pd

from config import CITIES
from extract import fetch_weather_data
from transform import transform_weather_data
from load import load_to_sqlite

def main():
    dataframes=[]

    for city in CITIES:
        city_name=city["name"]
        latitude=city["latitude"]
        longitude=city["longitude"]

        print(f"Fetching data for: {city_name}")

        raw_data=fetch_weather_data(latitude=latitude,longitude=longitude)
        city_df=transform_weather_data(raw_data=raw_data,city_name=city_name)

        dataframes.append(city_df)

    final_df=pd.concat(dataframes,ignore_index=True)

    print("\nCombined data:")
    print(final_df)

    load_to_sqlite(final_df)

    print(f"\nLoaded {len(final_df)} rows into database.")

if __name__=="__main__":
    main()