# Lead Programmer: Afton Lawver
# Program that inserts SP500 close price every 5 minutes into a database table

import sys
import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
import schedule
import time
# insert the path of the TerminalAIDatabase module into the syspath -------------------------------
# This inserts at runtime, so must import after this statement.
sys.path.insert(0, 'C:\Source\TerminalAI\PythonLibraries\Database\Database')
from TerminalAIDatabase import Database


def sp500_datetime():
    # Connect to database ----------------------------------------------------------------
    my_db = Database("C:\\Users\lawve\Desktop\Databases\mydb.db", show_messages=True)

    # Create a table ----------------------------------------------------------------
    '''
    my_db.create_table("SP500Datetime", ("Datetime", "Price"), ("TEXT", "REAL"))
    '''

    # Insert Row ----------------------------------------------------------------
        # Extract the data from tradingview every minute
    spx = TA_Handler(
        symbol = "SPX",
        screener = "CFD",
        exchange = "SP",
        interval = Interval.INTERVAL_1_DAY
    )
      # Get date and time of right now
    now = datetime.datetime.now() # now is a datetime object
    now_str = str(now) # Convert to string type
    analysis = spx.get_analysis()
    close_price = analysis.indicators["close"]
    my_db.insert_row('SP500Datetime', (now_str, close_price), ('Datetime', 'Price'))
    my_db.save_changes()
    my_db.close_database_connection()

'''
schedule.every(1).minute.at(':00').do(sp500_datetime)
while True:
    schedule.run_pending()

'''
def scrub(table_name:str):
        return ''.join(char for char in table_name if char.isalnum())

# def get_records_between_dates(name_of_table:str, start_datetime:str, end_datetime:str):
#     '''
#     Returns blah blah blah
#     '''
#     table = scrub(name_of_table)
#     my_parameters = (start_datetime, end_datetime)
#     query = "SELECT * FROM {} WHERE Date BETWEEN date(?) AND date(?);".format(table)
#     my_db.(query, my_parameters)
#     rows = my_db.fetch_all()
#     for row in rows:
#         print(row)

# def get_records_after_date(name_of_table:str, start_date:str):
#     my_db.connect_to_database()
#     my_db.create_cursor()
#     my_parameters = (start_date,)
#     query = '''SELECT * FROM {} WHERE Date >= date(?);'''.format(table_name)
#     my_db.run_query(query, my_parameters)
#     rows = my_db.fetch_all()
#     for row in rows:
#         print(row)

# def get_records_before_date(name_of_table:str, end_date:str):
#     my_db.connect_to_database()
#     my_db.create_cursor()
#     my_parameters = (end_date,)
#     query = '''SELECT * FROM {} WHERE Date <= date(?);'''.format(table_name)
#     my_db.run_query(query, my_parameters)
#     rows = my_db.fetch_all()
#     for row in rows:
#         print(row)
   

def print_row():
    # Connect to database ----------------------------------------------------------------
    my_db = Database("C:\\Users\lawve\Desktop\Databases\mydb.db", show_messages=True)
    my_row = my_db.get_first_row('SP500Datetime')
    

def get_records_between_dates():
    my_db = Database("C:\\Users\lawve\Desktop\Databases\mydb.db", show_messages=True)
    my_rows = my_db.get_records_between_datetimes("SP500Datetime", "2022-01-01 14:15:00", "2022-01-01 14:30:00")

def get_records_after_datetime():
    my_db = Database("C:\\Users\lawve\Desktop\Databases\mydb.db", show_messages=True)
    my_rows = my_db.get_records_after_datetime("SP500Datetime", "2022-01-01 14:15:00")

def get_records_before_datetime():
    my_db = Database("C:\\Users\lawve\Desktop\Databases\mydb.db", show_messages=True)
    my_rows = my_db.get_records_before_datetime("SP500Datetime", "2022-01-01 14:15:00")

print("Records before:")
get_records_before_datetime()
print("Records after:")
get_records_after_datetime()