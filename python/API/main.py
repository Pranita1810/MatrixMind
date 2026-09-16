from fastapi import FastAPI, Depends
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,Session
from sqlalchemy import create_engine, String,Integer,select
from pydantic import BaseModel

# ------- ORM DB CONNECTION --------
class Base(DeclarativeBase):
    pass
class MyTable(Base):
    __tablename__="campaigns"
    campaign_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name        : Mapped[str] = mapped_column(String)
    due_date    : Mapped[str] = mapped_column(String)
    created_date: Mapped[str] = mapped_column(String)

engine = create_engine("sqlite:///campaign.db")

# create session to avoid repetative code
def getsession():
    with Session(engine) as session:
        yield session
#_________________________________________________


# ------ Pydantic BaseModel for data validation ------
class  DataVal(BaseModel):
    campaign_id : int | None = None
    name : str | None = None
    due_date : str | None = None
    created_date : str | None = None
#________________________________________________


app = FastAPI()

@app.get("/")
async def status():
    return {"Message": "Your API is now live"}

@app.get("/data")
async def data():
    with Session(engine) as session:
        result = session.execute(select(MyTable))
        return result.scalars().all()

@app.post("/Insert")
async def insert_data(data:DataVal, session: Session = Depends(getsession)):
    data = MyTable(
    campaign_id = data.campaign_id,
    name = data.name,
    due_date = data.due_date,
    created_date = data.created_date
    )
    session.add(data)
    session.commit()
    session.refresh(data)
    return data

@app.put("/data/updateall/{id}")
async def update_data(id : int ,data : DataVal, session : Session = Depends(getsession)):
    table = session.get(MyTable, id)
    table.name = data.name
    table.due_date = data.due_date
    table.created_date = data.created_date
    session.commit()
    session.refresh(table)
    return data

@app.patch("/data/update_partial/{id}")
async def update_data(id : int ,data : DataVal, session : Session = Depends(getsession)):
    table = session.get(MyTable, id)
    if data.name is not None:
        table.name = data.name

    if data.due_date is not None:
        table.due_date = data.due_date

    if data.created_date is not None:
        table.created_date = data.created_date
    session.commit()
    session.refresh(table)
    return table

@app.delete("/data/delete/{id}")
async def del_data(id : int, session : Session = Depends(getsession)):
    table = session.get(MyTable, id)
    if table is None:
        return {"Message" : "Data not found"}

    session.delete(table)
    session.commit()
    return {"Message" : "Data delete successfully"}