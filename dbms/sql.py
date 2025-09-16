'''
A script for handling the reading of sql scripts in python.
'''



import os
import sqlite3

class QueryManager:
    sql_dir = None
    sql_files = None

    def __init__(self, sql_dir):
        self.sql_dir = sql_dir
        # - Find all .sql files for the given directory and put them in a list
        self.sql_files = files = [
            f for f in os.listdir(self.sql_dir) if os.path.isfile(os.path.join(self.sql_dir, f)) and f.endswith('.sql')
        ]

    def __getattr__(self, item):
        """
           Lets query file be fetched by calling the query manager class object with the name of the query as the attribute
        """

        if item + '.sql' in self.sql_files:
            # - This is where the file is actually read
            with open(os.path.join(self.sql_dir, item + '.sql'), 'r') as f:
                return f.read()
        else:
            raise AttributeError(f'QueryManager cannot find file {str(item)}.sql')
    
    def get_commands(self, item):
        '''
        Return the commands in file item (excluding ".sql") as a string.
        '''
        commands = self.__getattr__(item)

        return commands
    
    def execute(self, database, item):
        '''
        Connects to a given database, performs the commands which are in a file with name given by item, and returns the result.
        '''
        conn = sqlite3.connect(database, isolation_level=None)
        commands = self.__getattr__(item)

        res = []
        for c in commands.split(";"):
            res += conn.execute(c).fetchall()
        conn.close()

        return res
    
    