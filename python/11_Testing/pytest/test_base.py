# ---- PYTHON TESTING USING PYTEST ----

"""
PyTest is a python's testing framework to build test cases and test any application or program. So basically
it checks if the output or requirement matches with the application or program or not if it does not it will raise fail.
We should use Test-Driven-Deployment where  we first build test cases and expected outputs and based on that we build our 
application. Application is only successful when all test cases are passed.
"""

import pytest 
from base import sorting, pg_connection, get_data, summ

# -- Basic Testing --
def test_sorting():
    temp_arr = [5,4,3,2,1,5,78,5,5]
    assert sorting(temp_arr) == sorted(temp_arr)


def test_connection_pg4():
    assert pg_connection(result=5) == 1


def test_data():
    import pandas as pd
    df = get_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df.columns) > 0
    assert len(df) == 12575


# pytest fixture
@pytest.fixture
def sales_data():
    return [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]
def test_sales_count(sales_data):
    assert len(sales_data) == 2
def test_total_sales(sales_data):
    assert sum(row["amount"] for row in sales_data) == 300


# pytest parameterize
@pytest.mark.parametrize("a,b, expected",[
    (1,2,3),
    (5,5,10),
    (101,99,200)
])
def test_addition(a,b,expected):
    assert summ(a,b) == expected



if __name__ == "__main__":
    test_sorting()