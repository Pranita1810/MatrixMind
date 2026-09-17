from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.object_mapper_connections import MyTable

# -- Status --
def status():
    return {"Message": "Your API is now live"}

# -- Get All Data --
def get_data(session: Session):
    result = session.execute(select(MyTable))
    return result.scalars().all()

# -- Get Data by ID --
def get_data_id(id: int, session: Session):
    return session.get(MyTable, id)

# -- Add New Data --
def insert_data(body, session: Session):
    new_data = MyTable(
        date=body.date,
        datetime=body.datetime,
        cash_type=body.cash_type,
        card=body.card,
        money=body.money,
        coffee_name=body.coffee_name
    )
    session.add(new_data)
    session.commit()
    session.refresh(new_data)
    return new_data

# -- Update Data --
def update_data(id: int, body, session: Session):
    data = session.get(MyTable, id)
    if not data:
        return None
    data.date = body.date
    data.datetime = body.datetime
    data.cash_type = body.cash_type
    data.card = body.card
    data.money = body.money
    data.coffee_name = body.coffee_name
    session.commit()
    session.refresh(data)
    return data

# -- Delete Data --
def delete_data(id: int, session: Session):
    data = session.get(MyTable, id)
    if not data:
        return None
    session.delete(data)
    session.commit()
    return {"Message": "Data deleted successfully"}