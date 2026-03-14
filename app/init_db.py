import sqlite3
from pathlib import Path

from app.logger import get_logger
from app.settings import DB_PATH

logger=get_logger(__name__)

BASE_DIR=Path(__file__).resolve().parent.parent
SCHEMA_PATH=BASE_DIR/"sql"/"schema.sql"

def init_database():
    with sqlite3.connect(DB_PATH) as connection:
        with open(SCHEMA_PATH,"r",encoding="utf-8") as file:
            schema_sql=file.read()
        connection.executescript(schema_sql)

    logger.info(f"Database initialized successfully: {DB_PATH}")

if __name__=="__main__":
    init_database()