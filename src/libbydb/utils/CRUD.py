'''
The purpose of this script is to provide the user with functionality for performing various operations on the datbase,
i.e. create user, update employee information, etc.

The CRUD operations are the basic database operations:

CREATE: Add new data to the database. Done with the CREATE function.

READ: Retrieve instances from the database. Not implemented.

UPDATE: Change instances that are already in the datbase. Not implemented.

DELETE: Remove instances from the database. Not implemented.
'''

#%%
# SETUP
from libbydb.utils.sql import query, query_and_parse
import json
from datetime import datetime, timedelta


# %%
def CREATE(table: str, variables: list, values: list):
    '''
    This is a general function used to create a new instance in a given table in the database through an SQL query.
    '''

    # Error handling
    if len(variables) != len(values): raise ValueError("Incompatible variables and values. The number of variables and values must be the same.")
    if any([type(var) != str for var in variables]): raise ValueError("At least one variable was *not* str.")


    sql = f"INSERT INTO {table} ({", ".join(variables)}) VALUES ('{"\', \'".join(values)}')"
    return query(sql)

#%%
def READ(table: str, variables: list = None, where_variables: list = None, where_relations: list = None, where_values: list = None):
    '''
    This is a function that can be used to retrieve data from a specific table in the database.
    
    ARGUMENTS:
        table: The str name of the table to read from.

        variables: A list of variables to grab from the table. If unspecified, *all* columns will be returned.
    '''

    # Error handling
    if type(table) != str: raise ValueError("Argument 'table' must be a string.")

    # Parsing
    if variables == None: variables = "*"

    where_statement = ""
    if where_variables != None:
        if len(where_variables) != 0:
            statements = []
            for var, rel, val in zip(where_variables, where_relations, where_values):
                if type(val) in [int, float]: val = str(val)
                elif type(val) == str: val = f"'{val}'"
                statements.append(var + " " + rel + " " + val)
            
            where_statement = " WHERE " + " AND ".join(statements)

    sql = f"SELECT {", ".join(variables)} FROM {table}" + where_statement + ";"

    return query_and_parse(sql)
