import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR=Path(__file__).resolve().parent.parent
ENV_PATH=BASE_DIR/".env"

load_dotenv(ENV_PATH)

DB_PATH=BASE_DIR/os.getenv("DB_PATH","data/weather.db")
TABLE_NAME=os.getenv("TABLE_NAME","weather_data")
TIMEZONE=os.getenv("TIMEZONE","Europe/Warsaw")
API_TIMEOUT=int(os.getenv("API_TIMEOUT","10"))
LOG_LEVEL=os.getenv("LOG_LEVEL","INFO")