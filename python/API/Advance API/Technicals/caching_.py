# -- CACHING DATA --

""" 
we will go for HTTP Cache first then API Cache.
1. HTTP Cache : User's Browser | Content Delivery Network | Proxy Servers
2. API  Cache : Rdis | DataBase | FastAPI
"""

# ------------------ HTTP CACHING ------------------
from fastapi import FastAPI, Depends
from db_conn import MyTable, getsession
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import datetime as dt


class DataVal(BaseModel):
    date : dt.date | None = None
    datetime : dt.datetime | None=None
    cash_type : str
    card : str
    money : float
    coffee_name : str


app = FastAPI()


# User's Browser cache 
@app.get("/B_cache")
def browser_cache(
    session : Session = Depends(getsession)
):
    result = session.execute(select(MyTable)).scalars().all()
    result = JSONResponse(
        content=jsonable_encoder(result)
    )
    result.headers["Cache-Control"] = "public, max-age=6000"
    
    return result
# USAGE : when quick data access and don't want to hit any outside server again and again

# Proxy Server & CDN Server Cache
""" 
Here the python code is same the difference is we rout proxy & CDN server
to prod deployed API & setup nginx + cache in proxy & CDN server. so when client
send request to proxy or cdn it is routed to prod API and if client send requst
again first request go to proxy or cdn server and check if there is any cache 
if yes use it if not rout to prod API.
USAGE : when user don't want to hit prod level server again and again
"""




# ----------- APPLICATION CACHE -----------
# Internal cahce
cache = {}  
@app.get("/fastapi_cache")
def get_memory_cache(
    session : Session = Depends(getsession)
):
    """ Here we will use python's internal memroy to store cache
    so technically we are using memroy of machine where API is deployed"""
    if "data" in cache:
        return cache["data"]
    data = session.execute(select(MyTable)).scalars().all()

    cache["data"] = data
    return data
#USAGE : When no need to hit db again and again


# Redis cache
import redis
import json
r = redis.Redis(
    host="localhost",
    port = 6379,
    decode_responses=True
)

@app.get("/redis")
def get_redis_data(
    session: Session = Depends(getsession)
):
    cache_ = r.get("data")
    if cache_:
        print("CACHE HIT")
        return json.loads(cache_)
    print("CACHE MISS")

    # DB
    data = session.execute(
        select(MyTable)
    ).scalars().all()
    data = jsonable_encoder(data)
    r.set(
        "data",
        json.dumps(data, default=str),
        ex=60)

    return data


# -- db cache --
"""DB cache is handled internally by db itself 
we do not need to write separate code for this 
so usually when you write SELECT * FROM TABLE 
database bring data from cache itself internally.
"""



