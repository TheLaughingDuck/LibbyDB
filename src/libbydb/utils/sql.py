'''
This script contains functions that perform the SQL operations.
'''

#%%
# SETUP
import requests
import os
import logging
import json
import dotenv

# Define logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs/sql_logs.log", encoding="utf-8", level=logging.INFO)


def query(sql: str, DB_URL:str, DB_AUTH_TOKEN:str, args=None):
    '''
    Sends an sql query to the database, and returns the response.

    ARGUMENTS:
        sql: An SQL string that is sent to the DBMS. For example "SELECT (name) FROM users".

        DB_URL: Either the environment name of the database URL (hidden in a local .env file), or the raw database URL (i.e. "KJKASSDKBKABDKJBAKJADDJA...")

        DB_AUTH_TOKEN: Either the environment name for the appropriate authentication token, (hidden in a local .env file), or the raw authentication token (i.e. "KJKASSDKBKABDKJBAKJADDJA...")

        args: Optional extra arguments to the `requests.post` payload.

    Every query is logged in "WORKING_DIR/logs/sql_logs.log"
    '''
    
    try:
        # Try to load the secrets using dotenv, then grab database url and authentication token
        dotenv.load_dotenv()
        DATABASE_URL=os.getenv(DB_URL)
        AUTHENTICATION_TOKEN=os.getenv(DB_AUTH_TOKEN)
    except:
        # If loading the secrets failed, assume that the secrets were given directly in the arguments.
        DATABASE_URL = DB_URL
        AUTHENTICATION_TOKEN = DB_AUTH_TOKEN
    
    # Format headers for the `requests.put` payload.
    HEADERS = {
        'Authorization': f'Bearer {AUTHENTICATION_TOKEN}',
        'Content-Type': 'application/json'
    }

    
    payload = {
        'requests': [
            {
                'type': 'execute',
                'stmt': {
                    'sql': sql,
                    'args': args or []
                }
            },
            {'type': 'close'}
        ]
    }

    response = requests.post(f'{DATABASE_URL}/v2/pipeline', json=payload, headers=HEADERS)

    # Check if the request was successful
    if response.status_code == 200:

        # The query may have returned with multiple results. Check if any of them was an error.
        error_messages = []
        for r in json.loads(response.content)["results"]:
            if r["type"] == "error": error_messages.append(r["error"]["message"])
            elif r["type"] == "ok": pass
            else: print(f"Unknown result type {r["type"]} (This is probably fine).")
        
        if error_messages == []:
            logger.info(f"SQL query \"{sql}\" was SUCCESSFULLY carried out.")

        # There was at least one error
        else:
            if len(error_messages) == 1:
                logger.warning(f"SQL query \"{sql}\" encountered an ERROR: \"{error_messages[0]}\"")
            elif len(error_messages) > 1:
                # This has not been tested!
                logger.warning(f"SQL query \"{sql}\" encountered multiple ERRORS: {"\""+"\", and \"".join(error_messages) + "\""}")
        
        return response.json()
    else:
        # Log the SQL query and note that it was UNsuccessful
        logger.warning(f"SQL query \"{sql}\" FAILED.")

        raise Exception(f"Error executing query: {response.status_code} - {response.text}")


# def handle_response(response):
#     '''Handles the response from the Turso database.'''
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error executing query: {response.status_code} - {response.text}")


def query_and_parse(sql: str):
    '''
    Wrapper for `query`, useful when doing READ requests. Returns the response in a pandas dataframe.
    '''
    
    res = query(sql=sql)

    cols = [i["name"] for i in res["results"][0]["response"]["result"]["cols"]]
    rows = [[i["value"] if "value" in i.keys() else "null" for i in row] for row in res["results"][0]["response"]["result"]["rows"]]

    import pandas as pd

    df = pd.DataFrame(rows, columns=cols)
    return df