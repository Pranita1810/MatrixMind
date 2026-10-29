# Basic Funtions (Compare values)
def sorting(array : list) -> list:
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
    return array


# Connection function (connect posgres)
def pg_connection(result = None, connection = None):
    import sqlalchemy
    LOCALURL = "postgresql://postgres:pranit@localhost:5432/datawarehouse_sales"
    engine = sqlalchemy.create_engine(LOCALURL)
    if connection is not None:
        return engine
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT 1")).scalar_one()
    return result


# Data Function  
import pandas as pd
import sqlalchemy
def get_data():
    engine = pg_connection(connection="connect")
    with engine.connect() as conn:
        return pd.read_sql(sqlalchemy.text("SELECT * FROM sales") , conn)


#simple function
def summ(a,b):
    return a + b
