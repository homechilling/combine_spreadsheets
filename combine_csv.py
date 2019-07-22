# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:51:32 2019

get the data from two CSV files and merge them into one CSV

the two CSV files are combined on "First Name" and "Last Name" columns

@author: hao
"""

import pandas as pd

df1 = pd.read_csv("CSV1.csv") # first file
df2 = pd.read_csv("CSV2.csv") # second file

df_result = pd.merge(df1, df2, left_on = ['Last Name', 'First Name'], right_on = ['Last Name:', 'First Name:']) # merge two files on first/last names
df_result.drop('First Name:', axis=1, inplace=True) # remove redundant column
df_result.drop('Last Name:', axis=1, inplace=True) # remove redundant column

df_result.to_csv ("combined_spreadsheet.csv", index = None, header=True)
