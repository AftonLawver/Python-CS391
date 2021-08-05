# Lead Programmer: Afton Lawver 
'''
This program will allow the user to find out their unknown microorganism
by inputting test results. The output will be something like: your organism is x.
'''

import mysql.connector

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

    def __init__(self):
        pass


class BiochemicalTests():

    def __init__(self):
        pass

a = Database()
print(a)