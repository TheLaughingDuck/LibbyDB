'''
This script is used to create new instances in the library database,
like media, user, loan, employee.
'''

#%%
# SETUP
from Application.utils.sql import query, query_and_parse
import json
from datetime import datetime, timedelta
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
    due_date = str((datetime.today() + timedelta(days=loan_length)).date())
    sql1 = f" INSERT INTO loans (media_id, user_id, loan_date, due_date) VALUES ('{media_id}', '{user_id}', '{today_str}', '{due_date}')"

    # Create loan object
    res1 = query(sql1)

    # Update media status
    sql2 = f" UPDATE media SET loaned = 'TRUE' WHERE id = {media_id}"
    res2 = query(sql2)

    return [res1, res2]


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


def return_media(media_id):
    '''
    This function returns a media instance in the library database.
    '''
    # Check if the media exists and is currently loaned out
    sql_check = f" SELECT * FROM loans WHERE media_id = {media_id} AND resolved = 'FALSE'"
    df = query_and_parse(sql_check)

    if df.empty:
        print(f"No active loan found for media ID {media_id}.")
        return
    if df.shape[0] > 1:
        print(f"Multiple active loans found for media ID {media_id}.")
        return

    loan_id = df["id"].tolist()[0]

    # Update media status
    sql1 = f" UPDATE media SET loaned = 'FALSE' WHERE id = {media_id}"
    res1 = query(sql1)

    # Set loan as returned
    sql2 = f" UPDATE loans SET resolved = 'TRUE' WHERE id = {loan_id}"
    res2 = query(sql2)
    
    # Set loan return date
    sql3 = f" UPDATE loans SET return_date = '{datetime.today().date()}' WHERE id = {loan_id}"
    res3 = query(sql3)

    print(f"Media id {media_id} has been returned and loan id {loan_id} has been resolved.")
    return #[res1, res2, res3]


# %%
