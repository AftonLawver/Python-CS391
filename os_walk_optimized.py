# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:35:47 2020

@author: Afton Lawver
"""
import sys
import os
import pandas as pd
from datetime import datetime
import pandas as pd
from pandas import *
import os.path
import pathlib
from pathlib import Path
import time


# filename = sys.argv[1] 

def Set_Directory(filename):
    search_path = str(Path.home()) +'\Desktop'
    result = []
    
# Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
            r = result
            listToStr = ''.join([str(elem) for elem in r])
            directory = os.path.dirname(listToStr)
            os.chdir(directory)
            print(directory)
            return directory
        else:
            print("file does not exist")

x = Set_Directory("test.txt")
print(x)

# def CreateCSV(filename):
#     x = ['Day of week', 'Month', 'Day of month', 'Year', 'Time in A', 
#            'Time out A', 'Time Worked A', 'Task Worked on A', 'Time in B', 
#            'Time out B', 'Time Worked B', 'Task Worked on B']
#     df = pd.DataFrame(columns= x)
#     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
#     os.chdir(desktop)
# # Allow the user to specify where they want the files saved at
#     # question = input("Would you like to put the file in a new folder on the Desktop? (yes or no): ")   
#     # if question == 'yes':
#     #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
#     #     os.chdir(desktop)
#     #     where = input("What would you like the folder to be named?: ")
#     #     os.mkdir(where)
#     #     os.chdir(os.getcwd() + '\\' + where)
#     #     df.to_csv(filename)
#     # else: 
#     #     print("Current directory is", os.getcwd())
#     #     directory = input("Where would you like to save the newly created timesheet file?: ")
#     #     os.chdir(directory)
#     df.to_csv(filename)
    
# change filename based on when pay periods begin
# take input from user as to when they get paid (every two weeks, every week, etc.)
# automatically create a new file after x amount of days 

'''
def split(word):
    return [char for char in word]
    
def Clock_In(filename): 
    directory = Set_Directory(filename)
    


 
# Getting current time and date from the computer 
# Setting the current time and date into separate variables

    x = datetime.now()
    date = x.strftime("%A:%B:%d:%Y:%H:%M:%S")
    date_split = date.split(':')
    
# variables
    day_of_week = date_split[0]
    month = date_split[1]
    temp_day_of_month = date_split[2]
    temp_day_of_month = split(temp_day_of_month)
    if temp_day_of_month[0] == '0':
        temp_day_of_month.remove('0')
        day_of_month = temp_day_of_month[0]
    else:
        pass
    year = date_split[3]
    hour = date_split[4]
    minute = date_split[5]
    second = date_split[6]
    time = date_split[4:7]
    timein, timeout = ":".join(time), ":".join(time)
    
# Reading in the csv file as a dataframe, so that a value can be added into a specific cell
# Setting up the lastrow variable so it can be used for looking at the most up to date work day

    df = pd.read_csv(filename, index_col=[0])
    lastrow = df.tail(1)
    lastrow1 = lastrow.astype(str).values.flatten().tolist()
    shape = df.shape


    # if the shape (rows = 0), then add first row of data. 
    if shape[0] == 0:
        data = [[day_of_week, month, day_of_month, year, timein]] 
        x = ['Day of week', 'Month', 'Day of month', 'Year', 'Time in A']
        df1 = pd.DataFrame(data, columns= x)
        df = df.append(df1, ignore_index=True) 
        df.to_csv(filename)
        print("Clock in #1 successful.") 
        
    elif lastrow1[2] != day_of_month and lastrow1[1] == month:
        data = [[day_of_week, month, day_of_month, year, timein]] 
        x = ['Day of week', 'Month', 'Day of month', 'Year', 'Time in A']
        df1 = pd.DataFrame(data, columns= x)
        df = df.append(df1, ignore_index=True) 
        df.to_csv(filename)
        print("Created a new row for a new day. Clock in #1 successful.")
 
    elif lastrow1[1] == month and lastrow1[2] == day_of_month and lastrow1[4] != 'nan' and lastrow1[5] == 'nan':
        df.iloc[-1, df.columns.get_loc('Time out A')] = timeout
        df.to_csv(filename)
        print('Clock out 1 successful.')
        
        # Time worked block
        time_in_A1 = lastrow1[0:5]
        list_to_str = ' '.join([str(elem) for elem in time_in_A1])
        time_in_A11 = datetime.strptime(list_to_str, "%A %B %d %Y %H:%M:%S")
        time_elapsed = x - time_in_A11
        seconds = time_elapsed.total_seconds()
        hours = seconds/60/60
        hours_rounded = round(hours, 2)
        real_hours = '{}'.format(hours_rounded)
        df.iloc[-1, df.columns.get_loc('Time Worked A' )] = real_hours
        df.to_csv(filename)
        print("Time elapsed inserted for A.")
        
        # Task worked on block
        # task_a = input("What have you been working on?: ")
        # df.iloc[-1, df.columns.get_loc('Task Worked on A' )] = task_a
        # df.to_csv(filename)
   
    elif lastrow1[1] == month and lastrow1[2] == day_of_month and lastrow1[5] != 'nan' and lastrow1[8] == 'nan':
        df.iloc[-1, df.columns.get_loc('Time in B')] = timein
        df.to_csv(filename)
        print("Clock in #2 successful.")
        
    elif lastrow1[1] == month and lastrow1[2] == day_of_month and lastrow1[8] != 'nan' and lastrow1[9] == 'nan':
        df.iloc[-1, df.columns.get_loc('Time out B')] = timeout
        df.to_csv(filename)
        print("Clock out #2 successful.")
        
        # Time worked block
        listB = lastrow1[0:4]
        time_in_B1 = lastrow1[8] 
        listB.append(time_in_B1)
        list_to_str = ' '.join([str(elem) for elem in listB])
        time_in_B_as_datetime = datetime.strptime(list_to_str, "%A %B %d %Y %H:%M:%S")
        time_elapsed = x - time_in_B_as_datetime
        seconds = time_elapsed.total_seconds()
        hours = seconds/60/60
        hours_rounded = round(hours, 2)
        real_hours = '{}'.format(hours_rounded)
        df.iloc[-1, df.columns.get_loc('Time Worked B' )] = real_hours
        df.to_csv(filename)
        print("Time elapsed inserted for B.")
        
        # Task worked on block
        # task_b = input("What have you been working on?: ")
        # df.iloc[-1, df.columns.get_loc('Task Worked on B' )] = task_b
        # df.to_csv(filename)
        
    else:
        print("You have already worked a full day today.")


Clock_In('test.txt') 
 
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    


