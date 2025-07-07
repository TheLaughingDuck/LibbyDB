#%%
from . import sql
import pandas as pd

def test_query_and_parse():
    result = sql.query_and_parse("SELECT * FROM users")
    
    assert type(result) == pd.DataFrame


def test_query():
    result = sql.query("123")

    assert type(result) == dict