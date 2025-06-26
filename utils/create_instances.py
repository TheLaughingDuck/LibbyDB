'''
This script is used to create new instances in the library database,
like media, user, loan, employee.
'''

#%%
# SETUP
from sql import query
import json
from datetime import datetime
#%%

def create_media(name, description, type):
    '''
    This function creates a new media instance in the library database.
    '''
    today_str = str(datetime.today().date())
    sql = f" INSERT INTO media (name, owned_since, description, type) VALUES ('{name}', '{today_str}', '{description}', '{type}')"

    # Send sql
    res = query(sql)

    return res


def create_user(name, email):
    '''
    This function creates a new user instance in the library database.
    '''
    today_str = str(datetime.today().date())
    sql = f" INSERT INTO users (name, user_since, email) VALUES ('{name}', '{today_str}', '{email}')"

    # Send sql
    res = query(sql)

    return res


def create_loan(media_id, user_id, loan_length=28):
    '''
    This function creates a new loan instance in the library database.
    '''
    today_str = str(datetime.today().date())
    due_date = str((datetime.datetime.today() + datetime.timedelta(days=loan_length)).date())
    sql = f" INSERT INTO loans (media_id, user_id, loan_date, due_date) VALUES ('{media_id}', '{user_id}', '{today_str}', '{due_date}')"

    # Send sql
    res = query(sql)

    return res


def create_employee(name, title, reports_to, salary, salary_currency="SEK", employed_since=None):
    '''
    This function creates a new employee instance in the library database.
    '''
    today_str = str(datetime.today().date())
    if employed_since is None: employed_since = today_str
    sql = f" INSERT INTO employees (name, title, reports_to, salary, salary_currency, employed_since) VALUES ('{name}', '{title}', '{reports_to}', '{salary}', '{salary_currency}', '{employed_since}')"

    # Send sql
    res = query(sql)

    return res