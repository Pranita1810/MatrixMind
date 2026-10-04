# ---------- IMPORT REQUIREMENTS ----------
import os
import sys
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query, APIRouter
from fastapi.responses import StreamingResponse, Response
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from backend.app.db.orm_session import engine, getsession, get_model, getsession_user, WatchList_Table, TradeTable
import orjson
from backend.app.core.security import verify_access_token
from pydantic import BaseModel
import datetime as dt
import redis
import logging

logger = logging.getLogger("moneyhoney.users")

# ----- Add Backend Dir to sys path -----
BASE_DIR = Path(__file__).resolve().parents[4]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


# Define Pydantic Body
class WatchBody(BaseModel):
    user_id : int
    stock_symbol : str
    comments : str

# ------- REDIS CONNECTION --------
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=0,
    decode_responses=False,
    socket_timeout=1.0,
    socket_connect_timeout=1.0
)

router = APIRouter(tags=["Market & Users"])

# ----------- MAIN FAST APP -----------
app = FastAPI(
    title="MoneyHoney Data API",
    description="High-performance financial market data endpoints",
    version="1.0.0",
    root_path="/mh/v1"
)


# ----- Quick Status -----
@router.get("/home")
def status():
    return {"Message": "Application is live"}


# ----- Get Full Data of a Ticker -----
@router.get("/get_data/{ticker}")
def get_data(
    ticker: str,
    user=Depends(verify_access_token),
    session: Session = Depends(getsession),
    cursor: Optional[int] = Query(default=0),
    limit: int = Query(20, ge=1)
):

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    model = get_model(f"{ticker}_minute")

    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"{ticker} not found"
        )

    # Unique cache key for this request
    cache_key = f"ticker:{ticker}:cursor:{cursor}:limit:{limit}"

    # 1. Check Redis (gracefully handle if Redis is unavailable)
    try:
        cached_data = r.get(cache_key)
        if cached_data:
            return Response(
                content=cached_data,
                media_type="application/json",
                headers={"X-Cache": "HIT"}
            )
    except Exception as exc:
        logger.debug(f"Redis cache lookup failed: {exc}")

    # 2. Get data from database
    result = session.execute(
        select(model)
        .where(model.c.id > cursor)
        .order_by(model.c.id)
        .limit(limit)
    )

    data = []
    for row in result.mappings():
        data.append(dict(row))

    # 3. Convert to JSON bytes
    json_data = orjson.dumps(
        data,
        option=orjson.OPT_NON_STR_KEYS
    )

    # 4. Store in Redis for 60 seconds (gracefully ignore if Redis offline)
    try:
        r.setex(
            cache_key,
            60,
            json_data
        )
    except Exception as exc:
        logger.debug(f"Redis cache set failed: {exc}")

    # 5. Return response
    return Response(
        content=json_data,
        media_type="application/json",
        headers={"X-Cache": "MISS"}
    )


# ------ GET USER WATCHLIST ------
@router.get("/watchlist/{user_id}")
def get_watchlist(
    user_id: int,
    session: Session = Depends(getsession_user),
    user=Depends(verify_access_token)
):
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    result = session.execute(
        select(WatchList_Table)
        .where(WatchList_Table.user_id == user_id)
        .order_by(WatchList_Table.id)
    )

    return result.scalars().all()



# ------ GET TRADE HISTORY ------
@router.get("/mytrades/{user_id}")
def get_mytrades(
    user_id : int,
    session : Session = Depends(getsession_user),
    user = Depends(verify_access_token)
):
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    result = session.execute(
        select(TradeTable)
        .where(TradeTable.user_id == user_id)
        .order_by(TradeTable.id)
    )

    return result.scalars().all()



# -------- POST & PUT WATCHLIST ---------
# Add New Data
@router.post("/new")
def add_new(
    body : WatchBody,
    session : Session = Depends(getsession_user),
    user = Depends(verify_access_token)
):
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Not authorised"
        )

    new_watch = WatchList_Table(
        user_id=body.user_id,
        stock_symbol=body.stock_symbol,
        comments=body.comments
    )

    session.add(new_watch)
    session.commit()
    session.refresh(new_watch)

    return new_watch


# -------- PUT WATCHLIST BY ID --------
@router.put("/watchlist/{id}")
def update_watchlist(
    id: int,
    data: WatchBody,
    session: Session = Depends(getsession_user),
    user=Depends(verify_access_token)
):
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    watch = session.get(WatchList_Table, id)

    if not watch:
        raise HTTPException(
            status_code=404,
            detail="Watchlist item not found"
        )

    watch.user_id = data.user_id
    watch.stock_symbol = data.stock_symbol
    watch.comments = data.comments

    session.commit()
    session.refresh(watch)

    return watch


app.include_router(router)


    
    


