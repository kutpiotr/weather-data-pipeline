CREATE TABLE IF NOT EXISTS weather_data (
id INTEGER PRIMARY KEY AUTOINCREMENT,
city TEXT NOT NULL,
date TEXT NOT NULL,
temperature_max REAL,
temperature_min REAL,
precipitation_sum REAL,
created_at TEXT DEFAULT CURRENT_TIMESTAMP
);