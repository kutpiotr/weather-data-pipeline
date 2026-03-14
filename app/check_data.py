import sqlite3
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"

with sqlite3.connect(DB_PATH) as connection:
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM weather_data;")
    rows=cursor.fetchall()

for row in rows:
    print(row)