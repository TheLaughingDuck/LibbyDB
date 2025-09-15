'''
This script runs a loop that evaluates incoming SQL tasks. It is not supposed to be interactive, but rather, developers can issue commands that eventually
are executed, based on a priority-queue system.
'''

import time
import sqlite3
import os

# Setup SQl querying
from sql import QueryManager
sql_dir = os.path.join(os.path.dirname(__file__), 'sql_files')
qm = QueryManager(sql_dir)

status_message_interval = 10 # Number of seconds between each status message

def wh_server():
    # Startup messages
    print("Starting up DBMS.")
    start_time = time.time()
    status_message_time = time.time()

    ### STARTUP CHECKS
    # Build the warehouse and task queue, if they don't already exist.
    build_warehouse()

    # LOOP
    while (time.time() - start_time < 300):
        # PRINT STATUS MESSAGE every status_message_interval seconds
        if time.time() - status_message_time > status_message_interval:
            status_message_time = time.time()
            print("Status message.")

         
        # PERFORM ONE COMMAND
        do_command()


def build_warehouse():
    '''
    Create the tables in the database file, and the task queue database file.
    Tables are created only if they do not already exist.
    If they do already exist, this function should not break, and just ignore those tables.
    '''
    # Build warehouse database
    conn = sqlite3.connect("dbms/warehouse.sqlite", isolation_level=None)
    commands = qm.build_warehouse
    for c in commands.split(";"): conn.execute(c)
    conn.close()

    # Build Warehouse task queue database
    conn = sqlite3.connect("dbms/wh_task_queue.sqlite", isolation_level=None)
    commands = qm.build_warehouse_task_queue
    for c in commands.split(";"): conn.execute(c)
    conn.close()



def do_command():
    '''
    Finds the command with top priority among all queued commands, and performs it.
    '''

    queue_conn = sqlite3.connect("dbms/wh_task_queue.sqlite", isolation_level=None)
    queue_tasks = queue_conn.execute("SELECT * FROM task WHERE status = 'waiting'").fetchall()
    #queue_tasks = queue_conn.execute("SELECT * FROM task").fetchall()
    
    if len(queue_tasks) > 0:
        try:
            task = sorted(queue_tasks, key=lambda x: x[2])[0] # Sort by priority. 1 is the highest priority.
            #print(f"Attempting to perform task:'{task[1]}' (id: '{task[0]}', priority: '{task[2]}'), issued by user '{task[4]}'")
            print("\nAttempting to perform task:")
            print(f"\t{task[1]}")
            print(f"\tid: '{task[0]}'")
            print(f"\tpriority: '{task[2]}'")
            print(f"\tuser: '{task[4]}'")
        except:
            print(f"Some issue occurred while trying to perform a task.")
        
        # Try to perform the command
        try:
            wh_conn = sqlite3.connect("dbms/warehouse.sqlite", isolation_level=None)
        except:
            print("Failed to connect.")
        
        try:
            # Execute the SQL statements in the task
            for c in task[1].split(";"): wh_conn.execute(c)

            # Set the task as completed
            queue_conn.execute(f"UPDATE task SET status = 'completed' WHERE id = '{task[0]}'")

        except sqlite3.IntegrityError as e:
            print(f"There was a Sqlite Integrity Error, specifically \"{e}\"")
            queue_conn.execute(f"UPDATE task SET status='failed', response='{str(e)}' WHERE id = '{task[0]}'")
        except Exception as e:
            print(f"An unknown error occurred: {e}")
            queue_conn.execute(f"UPDATE task SET status='failed', response='{str(e)}' WHERE id = '{task[0]}'")


if __name__ == "__main__": wh_server()