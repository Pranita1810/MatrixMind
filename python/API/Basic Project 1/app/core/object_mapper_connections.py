import os
from dotenv import load_dotenv
from sqlalchemy import Integer, String, Float, create_engine, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, Session, DeclarativeBase
import datetime as dt
load_dotenv(override=True)

# --------- ORM & DB CONNECTIONS ---------
class Base(DeclarativeBase):
    pass

class MyTable(Base):
    __tablename__ = "Cafe_Data"
    cafe_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[dt.date] = mapped_column(Date)
    datetime: Mapped[dt.datetime] = mapped_column(DateTime)
    cash_type: Mapped[str] = mapped_column(String(50))
    card: Mapped[str] = mapped_column(String(50), nullable=True)
    money: Mapped[float] = mapped_column(Float)
    coffee_name: Mapped[str] = mapped_column(String(100))

database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(database_url, pool_pre_ping=True)

def getsession():
    with Session(engine) as session:
        yield session
