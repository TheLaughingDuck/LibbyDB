'''
This script contains functions that perform the SQL operations.
'''

#%%
# SETUP
import requests
import os
import logging
import json

# Define logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs/sql_logs.log", encoding="utf-8", level=logging.INFO)

# Grab database url and authentication token
TURSO_DATABASE_URL=os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN=os.getenv("TURSO_AUTH_TOKEN")
HEADERS = {
    'Authorization': f'Bearer {TURSO_AUTH_TOKEN}',
    'Content-Type': 'application/json'
}


def query(sql: str, args=None):
    '''
    This is a low level function (from the perspective of this DBMS) that executes an SQL query against the Turso database.

    Every query is logged in "LibbyDB/logs/sql_logs.log"
    '''
    
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

    response = requests.post(f'{TURSO_DATABASE_URL}/v2/pipeline', json=payload, headers=HEADERS)

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
        
        # if response.content["results"][0]["type"] == "error":
        #     error_message = response.content["results"][0]["error"]["message"]
        #     logger.warning(f"SQL query \"{sql}\" encountered an ERROR: \"{error_message}\"")
        # else:    
        #     # Log the SQL query and note that it was successful
        #     logger.info(f"SQL query \"{sql}\" was SUCCESSFULLY carried out.")

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
    res = query(sql=sql)

    cols = [i["name"] for i in res["results"][0]["response"]["result"]["cols"]]
    rows = [[i["value"] if "value" in i.keys() else "null" for i in row] for row in res["results"][0]["response"]["result"]["rows"]]

    import pandas as pd

    df = pd.DataFrame(rows, columns=cols)
    return df