# Lead Programmer: Afton Lawver 
'''
This program will allow the user to find out their unknown microorganism
by inputting test results. The output will be something like: your organism is x.
'''

import sqlite3
from urllib.request import pathname2url
import os

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

    def create_table(self, filename):
        pass

    def check_existence(self,filename):
        try:
            # Check if db exists
            dburi = 'file:{}?mode=rw'.format(pathname2url(self.filename))
            conn = sqlite3.connect(dburi, uri=True)
        except sqlite3.OperationalError:
            return None
            
        


class BiochemicalTests():

    def __init__(self):
        pass

a = Database()
if a.check_existence(a.filename) == None:
    a.create_connection(a.filename)
    print("connection created.")
else:
    print("did not create connection.")

