from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
import time

from db_conn import getsession, MyTable
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI()


# Rate-limit storage
rate_data = {}


# Fixed Window Rate Limiter
def fixed_window_rate(request: Request):

    ip = request.client.host
    current_time = time.time()

    if ip not in rate_data:
        rate_data[ip] = {
            "count": 1,
            "start_time": current_time
        }
        return

    data = rate_data[ip]

    if current_time - data["start_time"] >= 60:
        data["count"] = 1
        data["start_time"] = current_time
        return

    if data["count"] >= 2:
        return JSONResponse(
            status_code=429,
            content={"message": "Too many requests"}
        )

    data["count"] += 1


@app.get("/rate")
def get_limited_data(
    session: Session = Depends(getsession),
    request: Request = None
):
    response = fixed_window_rate(request)

    if response:
        return response

    return session.execute(select(MyTable)).mappings().all()