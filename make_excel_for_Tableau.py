'''
Excel is sometimes... annoying... to work with.
So instead of downloading multiple excel sheets
and combining them, this script will query the
databse for all the data, and then put that data
together in an excel file, with one table in each
sheet, which is what Tableau expects.
'''

#%%
# SETUP
import pandas as pd
from Application.utils import sql

PATH = 'C:/Users/jorst/Documents/Github/LibbyDB/'

# QUERY THE DATABASE FOR DATA
df_users = sql.query_and_parse("SELECT * FROM users")
df_media = sql.query_and_parse("SELECT * FROM media")
df_loans = sql.query_and_parse("SELECT * FROM loans")

#%%
#df_users = pd.read_csv(PATH+'users.csv')
#df_media = pd.read_csv(PATH+'media.csv')
#df_loans = pd.read_csv(PATH+'loans.csv')



# Construct an excel file with the data
# Each table will be in a separate sheet
with pd.ExcelWriter(PATH+"data.xlsx") as writer:
    df_users.to_excel(writer, sheet_name='Users', index=False)
    df_media.to_excel(writer, sheet_name='Media', index=False)
    df_loans.to_excel(writer, sheet_name='Loans', index=False)
# %%
