"""Once the redis server is up we can connect out python code to redis and use it as to store cache 
data."""

# Redis Connection
import redis
r = redis.Redis(host="localhost", db=0, port=6379)


# Store data in dict form
r.set("Name", "Pranit")
print(r.get("Name"))


# Store an entire df
import pandas as pd
import pickle
df = pd.read_excel(r"C:\Users\PANRIT\OneDrive\Desktop\pca_student_data.xlsx")
r.set("My_df", pickle.dumps(df))
print(pickle.loads(r.get("My_df")))
