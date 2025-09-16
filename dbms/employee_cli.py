'''
This script runs an Employee Command Line Interface that allows Employees to interact with the dbms.
'''

#%%
import sqlite3
import time
import uuid
import os

# Setup SQl querying
from sql import QueryManager
sql_dir = os.path.join(os.path.dirname(__file__), 'sql_files')
qm = QueryManager(sql_dir)

def send_command():
    queue_conn = sqlite3.connect("dbms/wh_task_queue.sqlite", isolation_level=None)

    id = uuid.uuid4()
    user_id = 123
    task = f"INSERT INTO loans (id, name, int_var) VALUES (''{uuid.uuid4()}'', ''The great gatsby'', 2)"
    priority = 3
    #cmd = f"INSERT INTO 'task' (id, task, priority, user) VALUES ('{id}', '{task}', '{priority}', '{user_id}');"
    #print(cmd)
    queue_conn.execute(f"INSERT INTO 'task' (id, task, priority, user) VALUES ('{id}', '{task}', '{priority}', '{user_id}');")

#%%

def cli():
    # Startup messages
    print("Starting up DBMS.")
    start_time = time.time()

    # LOOP
    while (time.time() - start_time < 300):
        print("\nWhat would you like to do?")
        inp = input(">")
        #inp = "media"

        if inp == "media": get_media()
        
        if inp == "help": help()

        if inp == "exit": break


def help():
    print("\nThese are the available commands:")
    print("\tmedia: prints information about all available media.")

def get_media():
    print("Retrieving media")
    media = qm.execute("dbms/warehouse.sqlite", "retrieve_media")

    for m in media:
        m = [str(i) for i in m]
        print(", ".join(m, ))

if __name__ == "__main__": cli()
# %%
