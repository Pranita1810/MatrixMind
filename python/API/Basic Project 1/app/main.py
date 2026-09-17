from fastapi import FastAPI, Depends, HTTPException, Header,Request, status as http_status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.object_mapper_connections import getsession, engine, Base
from app.core.sec_ import verify_key, verify_user
from app.services.client import (
    get_data,
    get_data_id,
    update_data,
    insert_data,
    delete_data,
    status,
)
import datetime as dt
from Logs.recorder_ import logger
import time
security = HTTPBasic()


# -- Define Data Validation --
class DataVal(BaseModel):
    date: dt.date | None = None
    datetime: dt.datetime | None = None
    cash_type: str
    card: str 
    money: float
    coffee_name: str


# -- MAIN API --
app = FastAPI(title="Cafe Data API", version="1.0.0")


# Status
@app.get("/home")
def main_status():
    return status()


# Get full data
@app.get("/FullData")
def get_all(
    session: Session = Depends(getsession),
    credentials: HTTPBasicCredentials = Depends(security),
):
    if not verify_user(credentials.username, credentials.password):
        raise HTTPException(
            status_code=http_status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return get_data(session=session)


# Get data by id
@app.get("/byid/{id}")
def get_by_id(
    id: int,
    session: Session = Depends(getsession),
    credentials: HTTPBasicCredentials = Depends(security),
):
    if not verify_user(credentials.username, credentials.password):
        raise HTTPException(
            status_code=http_status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    data = get_data_id(id=id, session=session)
    if data is None:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail=f"Data with id {id} not found",
        )
    return data


# Add new data
@app.post("/AddData", status_code=http_status.HTTP_201_CREATED)
def main_insert(
    body: DataVal,
    session: Session = Depends(getsession),
    api_key: str = Header(..., alias="api-key"),
):
    if not verify_key(api_key):
        raise HTTPException(
            status_code=http_status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key",
        )
    return insert_data(body, session)


# Update existing data
@app.put("/UpdateData/{id}")
def main_update(
    id: int,
    body: DataVal,
    session: Session = Depends(getsession),
    api_key: str = Header(..., alias="api-key"),
):
    if not verify_key(api_key):
        raise HTTPException(
            status_code=http_status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key",
        )
    updated = update_data(id, body, session)
    if updated is None:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail=f"Data with id {id} not found",
        )
    return updated


# Delete by id
@app.delete("/DeleteData/{id}")
def main_delete(
    id: int,
    session: Session = Depends(getsession),
    api_key: str = Header(..., alias="api-key"),
):
    if not verify_key(api_key):
        raise HTTPException(
            status_code=http_status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key",
        )
    result = delete_data(id, session)
    if result is None:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail=f"Data with id {id} not found",
        )
    return result

# -- LOG --
@app.middleware("http")
async def log_request(request : Request, call_next):
    start = time.time()
    logger.info(f"REQUEST :{request.method} {request.url}")
    respondse = await call_next(request)
    duration = time.time() - start

    logger.info(
        f"RESPONDSE : {respondse.status_code} |"
        f"Time : {duration :3f}s"
    )
    return respondse

