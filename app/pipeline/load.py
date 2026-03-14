import sqlite3

from app.settings import DB_PATH,TABLE_NAME

def load_to_sqlite(df,table_name=TABLE_NAME):
    with sqlite3.connect(DB_PATH) as connection:
        df.to_sql(table_name,connection,if_exists="append",index=False)