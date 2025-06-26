'''
This script contains functions that perform the SQL operations.
'''

#%%
# SETUP
import requests
import os

TURSO_DATABASE_URL=os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN=os.getenv("TURSO_AUTH_TOKEN")

HEADERS = {
    'Authorization': f'Bearer {TURSO_AUTH_TOKEN}',
    'Content-Type': 'application/json'
}


def query(sql, args=None):
    '''Executes a SQL query against the Turso database.'''
    
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
    return handle_response(response)


def handle_response(response):
    '''Handles the response from the Turso database.'''
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error executing query: {response.status_code} - {response.text}")


def query_and_parse(q):
    res = query(sql=q)

    cols = [i["name"] for i in res["results"][0]["response"]["result"]["cols"]]
    rows = [[i["value"] if "value" in i.keys() else "null" for i in row] for row in res["results"][0]["response"]["result"]["rows"]]

    import pandas as pd

    df = pd.DataFrame(rows, columns=cols)
    return df