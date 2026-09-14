# -- IMPORT LIBRARIES --
import os
import pandas as pd
import streamlit as st

# -- LOAD DATASET (PORTABLE PATH) --
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.abspath(os.path.join(current_dir, "..", "data.csv"))

if os.path.exists(data_path):
    main_df = pd.read_csv(data_path, encoding="latin1")
else:
    st.error(f"Data file not found at: {data_path}")
    st.stop()

# -- DESCRIPTIVE ANALYSIS --
if "Quantity" in main_df.columns and "UnitPrice" in main_df.columns:
    main_df["Total Sales"] = main_df["Quantity"] * main_df["UnitPrice"]

# -- STREAMLIT UI --
st.set_page_config(page_title="Descriptive Sales Analysis", layout="wide")
st.title("Descriptive Sales Analytics Dashboard")
st.dataframe(main_df, height=600)