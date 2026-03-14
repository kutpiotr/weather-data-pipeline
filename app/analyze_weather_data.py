import sqlite3
from pathlib import Path

import pandas as pd

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"

def run_query(query):
    with sqlite3.connect(DB_PATH) as connection:
        df=pd.read_sql_query(query,connection)
    return df

def main():
    all_data_query="""
    SELECT
        id,
        city,
        date,
        temperature_max,
        temperature_min,
        precipitation_sum,
        created_at
    FROM weather_data
    ORDER BY date;
    """

    summary_query="""
    SELECT
        COUNT(*) AS total_rows,
        MIN(date) AS min_date,
        MAX(date) AS max_date,
        ROUND(AVG(temperature_max),2) AS avg_temperature_max,
        ROUND(AVG(temperature_min),2) AS avg_temperature_min,
        ROUND(AVG(precipitation_sum),2) AS avg_precipitation_sum
    FROM weather_data;
    """

    city_summary_query="""
    SELECT
        city,
        COUNT(*) AS total_rows,
        ROUND(AVG(temperature_max),2) AS avg_temperature_max,
        ROUND(AVG(temperature_min),2) AS avg_temperature_min,
        ROUND(SUM(precipitation_sum),2) AS total_precipitation
    FROM weather_data
    GROUP BY city
    ORDER BY city;
    """

    daily_summary_query="""
    SELECT
        city,
        date,
        ROUND(AVG(temperature_max),2) AS avg_temperature_max,
        ROUND(AVG(temperature_min),2) AS avg_temperature_min,
        ROUND(SUM(precipitation_sum),2) AS total_precipitation
    FROM weather_data
    GROUP BY city,date
    ORDER BY date;
    """

    all_data_df=run_query(all_data_query)
    summary_df=run_query(summary_query)
    city_summary_df=run_query(city_summary_query)
    daily_summary_df=run_query(daily_summary_query)

    print("\nALL DATA")
    print(all_data_df)

    print("\nSUMMARY")
    print(summary_df)

    print("\nCITY SUMMARY")
    print(city_summary_df)

    print("\nDAILY SUMMARY")
    print(daily_summary_df)

if __name__=="__main__":
    main()