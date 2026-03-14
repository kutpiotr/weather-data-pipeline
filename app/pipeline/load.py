import sqlite3
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"

def load_to_sqlite(df,table_name="weather_data"):
    with sqlite3.connect(DB_PATH) as connection:
        df.to_sql(table_name,connection,if_exists="append",index=False)