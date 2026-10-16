import pandas as pd
import polars as pl
import redis 
import json

#Read a simple excel file and store is using pandas or polars
def get_data(module_):
    path = r"C:\Users\PANRIT\OneDrive\Desktop\pca_student_data.xlsx"
    if module_ == "PD":
        return pd.read_excel(path)
    if module_ == "PL":
        return pl.read_excel(path)
    


# Redis server connection
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)


# Set data in redis
df_pd = get_data("PD")
df_pl = get_data("PL")
r.set('PD_dataframe', df_pd.to_json(orient="records"))
r.set('PL_dataframe', df_pl.write_json())

# Get data
get_objectsPD = r.get('PD_dataframe')
get_objectsPL = r.get('PL_dataframe')
final_df_pd = pd.read_json(get_objectsPD)
final_df_pl = pl.DataFrame(json.loads(get_objectsPL))

print(final_df_pd)
print(final_df_pl)