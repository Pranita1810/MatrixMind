from pydantic import BaseModel
import datetime as dt
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from backend.app.db.orm_session import getsession_user, TradeTable
from backend.app.core.security import verify_access_token
from sqlalchemy.orm import Session


class TradeBody(BaseModel):
    user_id : int
    stock_symbol : str
    trade_type : str
    quantity : int
    price : float
    timestamp : dt.datetime



# -------- POST NEW TRADE --------
router = APIRouter(tags=["Trades"])

app = FastAPI(
    title="MoneyHoney Data API",
    description="High-performance financial market data endpoints",
    version="1.0.0",
    root_path="/mh/v1"
)

@router.post("/trade")
def add_trade(
    data: TradeBody,
    session: Session = Depends(getsession_user),
    user=Depends(verify_access_token)
):
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    new_trade = TradeTable(
        user_id = data.user_id,
        stock_symbol=data.stock_symbol,
        trade_type=data.trade_type,
        quantity=data.quantity,
        price=data.price,
        timestamp=data.timestamp
    )

    session.add(new_trade)
    session.commit()
    session.refresh(new_trade)

    return new_trade

app.include_router(router)