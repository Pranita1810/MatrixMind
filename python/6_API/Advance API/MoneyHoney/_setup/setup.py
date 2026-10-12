# ----- DOWNLOAD DATA FROM KAGGLE ------
import kagglehub

path = kagglehub.dataset_download(
    "debashis74017/stock-market-data-nifty-50-stocks-1-min-data",
    output_dir=r".\stock data"
)

print("Downloaded to:", path)



#--------- UPLOAD DATA TO SSMS ----------
import pandas as pd
import pyodbc
import glob
import os
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://localhost/STOCK_DATA"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

files = glob.glob(
    r"C:\Users\PANRIT\OneDrive\Desktop\stock data\*.csv"
)

print(f"Found {len(files)} CSV files")

for file in files:

    df = pd.read_csv(file)

    table_name = os.path.splitext(
        os.path.basename(file)
    )[0]

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded: {table_name}")

engine.dispose()

print("-" * 100)
print("Files uploaded successfully")