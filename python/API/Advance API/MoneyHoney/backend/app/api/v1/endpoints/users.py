# ---------- IMPORT REQUIREMENTS ----------
import sys
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from backend.app.db.orm_session import engine, getsession, get_model
import orjson
from backend.app.api.v1.endpoints.security import verify_access_token


# ----- Add Backend Dir to sys path -----
BASE_DIR = Path(__file__).resolve().parents[4]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))



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
    # user=Depends(verify_access_token),
    session: Session = Depends(getsession),
    cursor: Optional[int] = Query(default=0),
    limit: int = Query(20, ge=0)
):
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


# ------ Get My WatchList ------
@app.get("/watchlist")
def get_watchlist(
    session : Session = Depends(getsession)
):
    return None


