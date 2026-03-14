import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"data"/"weather.db"

st.set_page_config(page_title="Weather Data Dashboard",layout="wide")

@st.cache_data
def load_data():
    query="""
    SELECT
        city,
        date,
        temperature_max,
        temperature_min,
        precipitation_sum,
        created_at
    FROM weather_data
    ORDER BY date;
    """

    with sqlite3.connect(DB_PATH) as connection:
        df=pd.read_sql_query(query,connection)

    df["date"]=pd.to_datetime(df["date"])
    return df

df=load_data()

st.title("Weather Data Pipeline Dashboard")
st.write("Prosty dashboard oparty o dane pogodowe zapisane w bazie SQLite.")

if df.empty:
    st.warning("Brak danych w bazie. Najpierw uruchom pipeline.")
    st.stop()

cities=sorted(df["city"].dropna().unique())
selected_city=st.selectbox("Wybierz miasto",cities)

filtered_df=df[df["city"]==selected_city].copy()

st.subheader("Podstawowe metryki")

col1,col2,col3,col4=st.columns(4)

col1.metric("Liczba rekordów",len(filtered_df))
col2.metric("Średnia temp. max",round(filtered_df["temperature_max"].mean(),2))
col3.metric("Średnia temp. min",round(filtered_df["temperature_min"].mean(),2))
col4.metric("Suma opadów",round(filtered_df["precipitation_sum"].sum(),2))

st.subheader("Wykres temperatury maksymalnej")
chart_df=filtered_df.sort_values("date").set_index("date")[["temperature_max"]]
st.line_chart(chart_df)

st.subheader("Tabela danych")
st.dataframe(
    filtered_df.sort_values("date"),
    use_container_width=True
)