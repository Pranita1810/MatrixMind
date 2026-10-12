# Here we will work with databases using FastAPI
"""
To work with databases in FastAPI you have to understand what are ORM.
Object Relational Mapper let you work iwth SQL database using Python 
objects instead of writing SQL query for every operation.

For Example - [Without ORM : cursor.execute("SELECT * FROM TABLE")
               With ORM    : user = db.query(User).filter(User.id == 5).first()]

It converts Code to query. Now there are different ORMs but we will use
SQLAlchemy

""" 

# -- Import ORM --
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
from sqlalchemy import String, Integer
from sqlalchemy import create_engine, select


class Base(DeclarativeBase):
    pass

# - Map Python objects (telling SQLAlchemy how out data looks like) -
class campaign(Base):
    __tablename__ = "Campaigns"

    campaign_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String)
    due_date: Mapped[str] = mapped_column(String)
    created_date : Mapped[str] = mapped_column(String)

# - Create Database connection -
engine = create_engine("sqlite:///campaign.db")
Base.metadata.create_all(engine)      #-> Here alchemy wil create campaign.db & table in database

# - Session (Workspace where we perform DB operations)-
with Session(engine) as session:
    data = [
        campaign(campaign_id=1, name="Black Friday", due_date="2026-09-20", created_date="2026-09-02"),
        campaign(campaign_id=2, name="Diwali Sale", due_date="2026-10-15", created_date="2026-09-05"),
        campaign(campaign_id=3, name="Christmas Sale", due_date="2026-12-25", created_date="2026-09-10"),
        campaign(campaign_id=4, name="New Year Sale", due_date="2026-12-31", created_date="2026-09-12"),
        campaign(campaign_id=5, name="Republic Day", due_date="2027-01-26", created_date="2026-12-20"),
        campaign(campaign_id=6, name="Valentine's Day", due_date="2027-02-14", created_date="2027-01-10"),
        campaign(campaign_id=7, name="Holi Sale", due_date="2027-03-22", created_date="2027-03-01"),
        campaign(campaign_id=8, name="Summer Sale", due_date="2027-04-30", created_date="2027-04-01"),
        campaign(campaign_id=9, name="Monsoon Sale", due_date="2027-07-31", created_date="2027-07-01"),
        campaign(campaign_id=10, name="Independence Day", due_date="2027-08-15", created_date="2027-08-01"),
        campaign(campaign_id=11, name="Ganesh Chaturthi", due_date="2027-09-05", created_date="2027-08-20"),
        campaign(campaign_id=12, name="Navratri Sale", due_date="2027-10-10", created_date="2027-09-15"),
        campaign(campaign_id=13, name="Dussehra Sale", due_date="2027-10-15", created_date="2027-10-01"),
        campaign(campaign_id=14, name="Black Friday 2", due_date="2027-11-26", created_date="2027-11-01"),
        campaign(campaign_id=15, name="Cyber Monday", due_date="2027-11-29", created_date="2027-11-15"),
        campaign(campaign_id=16, name="Winter Sale", due_date="2027-12-15", created_date="2027-12-01"),
        campaign(campaign_id=17, name="Clearance Sale", due_date="2027-12-20", created_date="2027-12-05"),
        campaign(campaign_id=18, name="Mega Electronics Sale", due_date="2028-01-10", created_date="2027-12-20"),
        campaign(campaign_id=19, name="Back to School", due_date="2028-06-15", created_date="2028-05-20"),
        campaign(campaign_id=20, name="Anniversary Sale", due_date="2028-08-01", created_date="2028-07-01")
    ]
    session.add_all(data)
    session.commit()             # -> Behind this block "INSERT INTO campaigns (name, due_date) VALUES ('Holi Sales', '2026-09-20');"



# ---- READ DATA ----
with Session(engine) as session:
    data = session.scalars(select(campaign)).all()
    



# ------- IMP CONCEPTS -------
"""
1. create_engine()
   → Connect Python ↔ Database

2. Base / DeclarativeBase
   → Foundation for ORM models

3. Model class
   → Python representation of a DB table

4. mapped_column()
   → Defines a table column

5. Base.metadata.create_all(engine)
   → Create tables in DB

6. Session(engine)
   → Start a DB working session

7. session.add()
   → INSERT

8. session.commit()
   → Save changes permanently

9. select(Model)
   → SELECT

10. session.execute()
    → Execute the query

11. result.scalars().all()
    → Get multiple ORM objects

12. session.get(Model, id)
    → Get one row by primary key

13. Modify object + commit
    → UPDATE

14. session.delete() + commit
    → DELETE
"""