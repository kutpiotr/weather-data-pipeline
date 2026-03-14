from extract import fetch_weather_data
from transform import transform_weather_data
from load import load_to_sqlite

CITY_NAME="Rzeszow"
LATITUDE=50.0413
LONGITUDE=21.9990

def main():
    raw_data=fetch_weather_data(latitude=LATITUDE,longitude=LONGITUDE)
    df=transform_weather_data(raw_data=raw_data,city_name=CITY_NAME)

    print("Transformed data:")
    print(df)

    load_to_sqlite(df)

    print(f"\nLoaded {len(df)} rows into database.")

if __name__=="__main__":
    main()