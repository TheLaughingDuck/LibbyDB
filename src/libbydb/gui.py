'''
This script makes a simple GUI using Tkinter.
'''


#%%
# SETUP
import tkinter as tk
from tkinter import ttk
import datetime
import os
from utils import sql

today_str = str(datetime.datetime.today().date())

def main():
    app = App()
    app.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library User Interface")
        self.define_grid()
        self.pannel_info_box()
        self.create_destructive_actions_pannel()
        #self.define_make_object_pannel()

        self.pannel_make_user(row=1,col=0)
        self.pannel_make_loan(row=2, col=0)
        self.pannel_make_media(row=3, col=0)
        self.pannel_make_employee(row=4, col=0)

        self.state("zoomed") # Maximize the windowC

        #str(self.winfo_screenwidth()) + "x" + str(self.winfo_screenheight())
    
    
    def define_grid(self):
        for i in range(30):
            self.columnconfigure(i, weight=1)
        for i in range(30):
            self.rowconfigure(i, weight=1)
    
    # ==============================================================================
    # === VVV ==================== DEFINE PANELS =========================== VVV ===
    # ==============================================================================

    def pannel_info_box(self):
        ttk.Label(self, text="Date: " + today_str).grid(column=0, row=0, sticky='W')

    def pannel_make_user(self, row, col):
        frm = ttk.Frame(self)
        frm.grid(row=row, column=col, sticky='W')
        #ttk.Label(frm, text="Make a user").grid(column=0, row=0, sticky='N')
        ttk.Button(frm, text="Make user", command=self.make_user).grid(column=0, row=0)

        ttk.Label(frm, text="Name:").grid(column=0, row=1, sticky='W')
        tk.Text(frm, height=1, width=30).grid(column=1, row=1)

        ttk.Label(frm, text="email:").grid(column=0, row=2, sticky='W')
        tk.Text(frm, height=1, width=30).grid(column=1, row=2)
    
    def pannel_make_loan(self, row, col):
        frm = ttk.Frame(self)
        frm.grid(row=row, column=col, sticky='W')
        ttk.Button(frm, text="Make loan", command=self.make_loan).grid(column=0, row=0)

        ttk.Label(frm, text="Media id:").grid(column=0, row=1, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=1)

        ttk.Label(frm, text="User id:").grid(column=0, row=2, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=2)
    
    def pannel_make_media(self, row, col):
        frm = ttk.Frame(self)
        frm.grid(row=row, column=col, sticky='W')
        ttk.Button(frm, text="Make loan", command=self.make_loan).grid(column=0, row=0)

        ttk.Label(frm, text="Media id:").grid(column=0, row=1, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=1)

        ttk.Label(frm, text="User id:").grid(column=0, row=2, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=2)
    
    def pannel_make_employee(self, row, col):
        frm = ttk.Frame(self)
        frm.grid(row=row, column=col, sticky='W')
        ttk.Button(frm, text="Make employee", command=self.make_employee).grid(column=0, row=0)

        ttk.Label(frm, text="Name:").grid(column=0, row=1, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=1)

        ttk.Label(frm, text="Title:").grid(column=0, row=2, sticky='W') #SELECT
        tk.OptionMenu(frm, tk.StringVar(value="Title"), "Librarian", "Manager", "Assistant", "Bounty Hunter").grid(column=1, row=2)

        ttk.Label(frm, text="Reports to:").grid(column=0, row=3, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=3)

        ttk.Label(frm, text="Salary:").grid(column=0, row=4, sticky='W')
        tk.Text(frm, height=1, width=7).grid(column=1, row=4)

        ttk.Label(frm, text="Currency:").grid(column=0, row=5, sticky='W')
        tk.OptionMenu(frm, tk.StringVar(value="Currency"), "SEK", "EUR").grid(column=1, row=5)

        # Add a field for employed since

    # def define_make_object_pannel(self):
    #     frm = ttk.Frame(self)
    #     frm.grid(row=1, column=0)
    #     ttk.Button(frm, text="Make loan", command=self.make_loan).grid(column=0, row=2)
    #     ttk.Button(frm, text="Make user", command=self.make_user).grid(column=0, row=3)
    #     ttk.Button(frm, text="Make media", command=self.make_media).grid(column=0, row=4)
    #     ttk.Button(frm, text="Make employee", command=self.make_employee).grid(column=0, row=5)
    
    def create_destructive_actions_pannel(self):
        frm = ttk.Frame(self)
        frm.grid(row=0, column=29, sticky='N')
        ttk.Label(frm, text="Destructive actions").grid(column=0, row=0, sticky='N')
        ttk.Button(frm, text="Quit", command=self.destroy).grid(column=0, row=1)
    
    # ==============================================================================
    # === VVV ==================== SQL INSERT FUNCTIONS ==================== VVV ===
    # ==============================================================================

    def make_loan(self):
        # Make a loan
        print("Making a loan...")
    
    def make_user(self):
        # Make a user
        print("Making a user...")
    
    def make_media(self):
        # Make a media
        print("Making a media...")

    def make_employee(self):
        # Make an employee
        print("Making an employee...")


class App_v2(tk.Tk):
    '''
    An updated App class, intended to be more general, and to be able to generate a neat user interface by inferring the database schema from the tables.
    '''
    def __init__(self, tables:list, DB_URL:str, DB_AUTH_TOKEN:str, title="Database GUI"):
        # SET UP GUI
        super().__init__()
        self.title(title)

        # SET UP querying
        self.DB_URL = DB_URL
        self.DB_AUTH_TOKEN = DB_AUTH_TOKEN
        self.tables = tables
        self.schema = self.get_db_schema()

        # RENDER pannels
        self.pannel_CREATE()
    
    def get_db_schema(self):
        '''
        Grab the database schema, i.e. grab instances from each table in order to see what columns they have.
        '''
        schema = {}
        for table in self.tables:
            sql_string = f"SELECT * FROM {table} LIMIT 1"
            result = sql.query_and_parse(sql=sql_string, DB_URL=self.DB_URL, DB_AUTH_TOKEN=self.DB_AUTH_TOKEN)

            schema[table] = result.columns.tolist()
        
        return schema
        

    def pannel_CREATE(self):
        '''
        Creates a pannel of boxes for each table in the database, which can be used to create new instances.
        '''
        for table in self.schema:
            pass




if __name__ == "__main__":
    main()
# %%
