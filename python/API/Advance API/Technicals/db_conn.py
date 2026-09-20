# ---- COMMON DB CONNECTION -----
from sqlalchemy.orm  import Mapped, mapped_column, DeclarativeBase,Session
from sqlalchemy import String,Integer,Float,Date,DateTime,create_engine
import datetime as dt
from sqlalchemy import select


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

database_url = "mssql+pyodbc://api_user:1234@localhost:1433/test?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(database_url, pool_pre_ping=True)

def getsession():
    with Session(engine) as session:
        yield session


