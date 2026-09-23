from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()


# ------- CREATE MAIN ENGINE -------

url = os.getenv("DATABASE_URL_LOCAL")
engine = create_engine(url, pool_pre_ping=True)

def getsession():
    with Session(engine) as session:
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
from sqlalchemy import String, Integer, Float

class Base(DeclarativeBase):
    pass

class UserTable(Base):
    __tablename__="user_watchlist"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer)
    stock_symbol : Mapped[str] = mapped_column(String)
    comments : Mapped[str] = mapped_column(String)

