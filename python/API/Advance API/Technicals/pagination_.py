# ---- API PAGINATION ------
""" 
API Pagination happens entirely in database where
we set API to only retrieve chunks of data based on
user's need using OFFSET & CURSOR
"""

from fastapi import FastAPI, Depends, Query
from db_conn import  MyTable, getsession
from sqlalchemy import select
from sqlalchemy.orm import Session


app = FastAPI()


# ---- OFFSET -----
@app.get("/pagi-off")
def get_offset(
    session : Session = Depends(getsession),
    skip : int = Query(0,ge=0),                #skip n rows
    limit : int = Query(20, ge=1,le=100)       #only keep n rows after skipping n rows
):
    query = (
        select(MyTable).order_by(MyTable.cafe_id)
        .offset(skip)
        .limit(limit)
    )
    return session.execute(query).mappings().all()


# ----- CURSOR ------
@app.get("/cursor")
def cursor_pagination(
    session : Session = Depends(getsession),
    skip : int = Query(None),
    limit : int = Query(20,ge=1,le=100)
):
    query = (select(MyTable).order_by(MyTable.cafe_id).limit(limit))

    return session.execute(query).mappings().all()
    
    