# ---------- IMPORT REQUIREMENTS ----------
import sys
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from backend.app.db.orm_session import engine, getsession, get_model, getsession_user, WatchList_Table, TradeTable
import orjson
from backend.app.core.security import verify_access_token
from pydantic import BaseModel
import datetime as dt



# ----- Add Backend Dir to sys path -----
BASE_DIR = Path(__file__).resolve().parents[4]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


# Define Pydantic Body
class WatchBody(BaseModel):
    id : int
    user_id : int
    stock_symbol : str
    comments : str




# ----------- MAIN FAST APP -----------
app = FastAPI(
    title="MoneyHoney Data API",
    description="High-performance financial market data endpoints",
    version="1.0.0",
    root_path="/mh/v1"
            )


# ----- Quick Status -----
@app.get("/home")
def status():
    return {"Message": "Application is live"}


# ----- Get Full Data of a Ticker -----
@app.get("/get_data/{ticker}")
def get_data(
    ticker: str,
    user=Depends(verify_access_token),
    session: Session = Depends(getsession),
    cursor: Optional[int] = Query(default=0),
    limit: int = Query(20, ge=0)
):
    if user :
        model = get_model(f"{ticker}_minute")

        if model is None:
            raise HTTPException(
                status_code=404,
                detail=f"{ticker} not found"
            )

        def generate():
            result = session.execute(
                select(model)
                .where(model.c.id > cursor)
                .order_by(model.c.id)
                .limit(limit)
            )

            yield b"["

            first = True

            for row in result.mappings():
                if not first:
                    yield b","

                yield orjson.dumps(
                    dict(row),
                    option=orjson.OPT_NON_STR_KEYS
                )

                first = False

            yield b"]"

        return StreamingResponse(
            generate(),
            media_type="application/json"
        )
    raise HTTPException(
        status_code=401,
        detail="Invalid user"
    )


# ------ GET USER WATCHLIST ------
@app.get("/watchlist/{user_id}")
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
@app.get("/mytrades/{user_id}")
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
@app.post("/new")
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


# Update user id
# -------- PUT WATCHLIST BY ID --------
@app.put("/watchlist/{id}")
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

    
    


