'''
This script contains test functions for the utils functions, i.e. the CRUD functions as well as the `query` and `query_and_parse` functions.
'''

import pytest

from . import sql
import pandas as pd
def test_query_and_parse():
    result = sql.query_and_parse("SELECT * FROM users")
    
    assert type(result) == pd.DataFrame


def test_query():
    result = sql.query("123")

    assert type(result) == dict


from . import CRUD
def test_CREATE():

    # Should fail if the "variables" argument is not given.
    with pytest.raises(Exception):
        result = CRUD.CREATE(table="users", values=["123"])
    
    # Should fail if the "values" argument is not given.
    with pytest.raises(Exception):
        result = CRUD.CREATE(table="users", variables=["123"])
    
    # Should fail if the "variables" and "values" arguments don't match in length.
    with pytest.raises(Exception):
        result = CRUD.CREATE(table="users", variables=["a", "b"], values=["c", "d", "e"])
    
    # Should fail if variables contains non-str values. 
    with pytest.raises(Exception):
        result = CRUD.CREATE(table="users", variables=["a", 678, "c"], values=["h", "k", "l"])


def test_READ():

    # Should work
    result = CRUD.READ("users", variables=["id", "name", "user_since"], where_variables=["warnings", "user_until"], where_relations=[">=", "="], where_values=[0, "null"])
    