from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime 

load_dotenv()


# ------- CREATE MAIN ENGINE -------

url_stock = os.getenv("DATABASE_URL_LOCAL")
user_url = os.getenv("DATABASE_URL_USERS")

def normalize_db_url(url: str | None) -> str:
    if not url:
        return ""
    # In Docker container on Windows/Linux, replace localhost with host.docker.internal
    if (os.path.exists('/.dockerenv') or os.getenv("REDIS_HOST") == "redis") and "localhost" in url:
        url = url.replace("localhost", "host.docker.internal")
    return url

_stock_engine = None
_user_engine = None

def get_stock_engine():
    global _stock_engine
    if _stock_engine is None:
        stock_url = os.getenv("DATABASE_URL_LOCAL") or os.getenv("DATABASE_URL_DOCKER")
        _stock_engine = create_engine(
            normalize_db_url(stock_url),
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20
        )
    return _stock_engine

def get_user_engine():
    global _user_engine
    if _user_engine is None:
        users_url = os.getenv("DATABASE_URL_USERS") or os.getenv("DATABASE_URL_USERS_DOCKER")
        _user_engine = create_engine(
            normalize_db_url(users_url),
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20
        )
    return _user_engine

def engine(url=None):
    if url and ("MHUsers" in url or "users" in url.lower()):
        return get_user_engine()
    return get_stock_engine()

# Stock session
def getsession():
    with Session(get_stock_engine()) as session:
        yield session

# User session
def getsession_user():
    with Session(get_user_engine()) as session:
        yield session


# -------- GET ORM --------
from backend.app.core.models.generated_models import *
import backend.app.core.models.generated_models as gen_models

def get_model(table_name: str):
    clean = table_name.strip()
    candidates = [
        clean,
        clean.upper(),
        clean.lower(),
        f"t_{clean}",
        f"t_{clean.upper()}",
        f"{clean}_minute",
        f"{clean.upper()}_minute",
        f"t_{clean}_minute",
        f"t_{clean.upper()}_minute",
    ]
    # Check globals
    g = gen_models.__dict__
    for name in candidates:
        model = g.get(name)
        if model is not None:
            return model

    # Check metadata case-insensitively
    meta_lookup = {k.lower(): v for k, v in metadata.tables.items()}
    for name in candidates:
        if name.lower() in meta_lookup:
            return meta_lookup[name.lower()]
    return None




# ------ GET USER ORM --------
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime

class Base(DeclarativeBase):
    pass

class WatchList_Table(Base):
    __tablename__="user_watchlist"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer)
    stock_symbol : Mapped[str] = mapped_column(String)
    comments : Mapped[str] = mapped_column(String)

class TradeTable(Base):
    __tablename__= "trades"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer)
    stock_symbol : Mapped[str] = mapped_column(String)
    trade_type : Mapped[str] = mapped_column(String)
    quantity : Mapped[int] = mapped_column(Integer)
    price : Mapped[float] = mapped_column(Float)
    timestamp : Mapped[datetime] = mapped_column(DateTime) 

