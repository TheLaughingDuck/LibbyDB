'''
This script runs a developer Command Line Interface that allows developers to interact with the dbms.
'''
#%%
import sqlite3
import time
import uuid

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
    start_time = time.time()

    # As a test.
    send_command()
    

    # while (time.time() - start_time < 30):
    #     #print("Looping")
    #     pass

if __name__ == "__main__": cli()
# %%
