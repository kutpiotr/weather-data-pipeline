import sqlite3
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"
SCHEMA_PATH=BASE_DIR/"sql"/"schema.sql"

def init_database():
    with sqlite3.connect(DB_PATH) as connection:
        with open(SCHEMA_PATH,"r",encoding="utf-8") as file:
            schema_sql=file.read()
        connection.executescript(schema_sql)
    print(f"Database initialized successfully: {DB_PATH}")

if __name__=="__main__":
    init_database()