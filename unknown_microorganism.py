# Lead Programmer: Afton Lawver 
'''
This program will allow the user to find out their unknown microorganism
by inputting test results. The output will be something like: your organism is x.
'''

import sqlite3
from urllib.request import pathname2url
import os
import pandas as pd

# 1. Write a database class that allows us to: 
#   a. Create a database that will hold information about all of the micro
#   organisms. 
#   b. Add a row to the database, add column to the database, add value(cell) to the database,
#      get value(cell) from database, get row from database, and get column from database.
#      

# 2. Write BiochemicalTest class: 
#   a. create biochemical test objects 
#   b. Have methods like isTestNamePositive
#   c. At the end of all of these tests, create a list of the test results and compare with
#      the database. 
#   d. Whichever bacteria has the greatest number of matching results, output that bacteria.

class Database():
    filename = r'TestDB.db'
    cwd = os.getcwd()
    cols = ['name', 'shape', 'gram']

    def __init__(self):
        # 
        #     print("creating db...")
        #     # connection = sqlite3.connect('TestDB.db')
        #     c = connection.cursor()

        #     # Create table - MICROORGANISMS
        #     c.execute('''CREATE TABLE MICROORGANISMS
        #     ([generated_id] INTEGER PRIMARY KEY, [MICROORGANISM NAME] text, [GRAM STAIN] text)''')

        #     c.commit()
        #     print("created db in {}".format(self.cwd))
        # try:
        #     sqlite3.connect('TestDB.db')
        #     print("database connected.")
        pass

    def create_connection(self, filename):
        conn = None
        try:
            conn = sqlite3.connect(self.filename)
            return conn
        except Exception as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

    def check_existence(self,filename):
        value = False
        try:
            # Check if db exists
            dburi = 'file:{}?mode=rw'.format(pathname2url(self.filename))
            conn = sqlite3.connect(dburi, uri=True)
            value = True
        except sqlite3.OperationalError:
            return value
    
    def get_table(self, conn):
        df = pd.read_sql("SELECT * FROM microorganisms", conn)
        return df

    def add_row(self, conn, cols, values):
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO TestDB.db.microorganisms ''' + (cols) + ''')
        VALUES''' + values)

    def add_column(self):
        pass


class BiochemicalTests():  
    def __init__(self):
        pass


def main():
    a = Database()
    if a.check_existence(a.filename) == False:
        conn = a.create_connection(a.filename)
        print("{} created in {}".format(a.filename, a.cwd))

        sql_microorganisms_table = """ CREATE TABLE IF NOT EXISTS           microorganisms (
            name TEXT NOT NULL,
            shape TEXT NOT NULL,
            gram stain TEXT NOT NULL);
            """
        a.create_table(conn, sql_microorganisms_table)
        print("table created.")

        # get the table to print out as a dataframe
        table = a.get_table(conn)
        print(table)
    else:
        conn = a.create_connection(a.filename)
        # get the table to print out as a dataframe
        table = a.get_table(conn)
        print('before addition')
        print(table)

        # add a new row to the dataframe
        a.add_row(conn, a.cols, ('E.coli', 'Rod', 'Negative'))
        table2 = a.get_table(conn)
        print('after addition')
        print(table)

if __name__ == '__main__':
    main()
