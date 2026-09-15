from fastapi import FastAPI
from fastapi import Request
from datetime import datetime
import random

app = FastAPI(root_path="/api/v1")


# Testing Data
data = [
    {
    "campaign_id":1,
     "name" : "Summer launch",
     "due_date": datetime.now(),
     "created_at": datetime.now()
     },
    {
    "campaign_id":2,
     "name" : "Diwali Sale",
     "due_date": datetime.now(),
     "created_at": datetime.now()
     }
]


# API status
@app.get("/")
async def root():
    return {"Message" : "Your API is now live"}

# This will response full data
@app.get("/data")
async def read_camp():
    return data

# Get only specific data (get data by id) 
@app.get("/data/{id}")
async def read_camp_id(id:int):
    for camp in data:
        if camp.get("campaign_id") == id:
            return camp
    return {"Message": "ID not found"}

# Add data using POST 
@app.post("/data/insert")
async def create_data(body : dict[str,str]):
    new = {
        "campaign_id": random.randint(3,30),
             "name" : body.get("name"),
             "due_date": body.get("due_date"),
             "created_at": datetime.now()
    }
    data.append(new)
    return data

# Update data using PUT
@app.put("/data/update/{id}")
async def update_data(id : int , body: dict[str, str]):
    for d in data:
        if d.get("campaign_id") == id:
            d["name"] = body.get("name")
            d["due_date"] = body.get("due_date")
            d["created_at"] = datetime.now()
            return d
    return {"Message" : "ID not found"}

# Delete data using delete method
@app.delete("/data/delete/{id}")
async def del_data(id:int):
    for d in data:
        if d.get("campaign_id") == id:
            data.remove(d)
            return {"Message" : "Data deleted successfully"}
    return {"Message" : "Failed to delete"}