#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: August 06, 2023
Assignment 08
PART I

"""

import pandas as pd
import re
from collections import defaultdict


# PART I


# Create Columns
employeecolumnnames = ['First', 'Middle', 'Last', 'SSN', 'DOB', 'Address', 'City', 'State', 'Gender', 'Salary', 'Unknown1', 'Years']

# Read File
employeefile = pd.read_csv("Employee.txt", sep = ",", names = employeecolumnnames, skipinitialspace = True)


# Change To DF
employeedf = pd.DataFrame(data = employeefile)


# Update Data Types for all Integers in DF
employeedf[['SSN', 'Salary', 'Years']] = employeedf[['SSN', 'Salary', 'Years']].astype(int)




#print the entire DF
print(employeedf)
print(" ")

# Question A - Find all male employees

for i in range(len(employeedf)): 
    if re.search('M', employeedf['Gender'][i]): 
        print(employeedf['First'][i], employeedf['Middle'][i], employeedf['Last'][i])

print("")

# Question B - Find the highest salary for female employees
femalesalary = {}

for i in range(len(employeedf)): 
    if re.search('F', employeedf['Gender'][i]):
        femalesalary[employeedf['SSN'][i]] = (employeedf['Salary'][i])
        
for e in range(len(employeedf)): 
    if employeedf['SSN'][e] == max(femalesalary, key = femalesalary.get): 
        print(employeedf['SSN'][e], employeedf['First'][e], employeedf['Middle'][e], employeedf['Last'][e], employeedf['Salary'][e])

print("")  

# Question C - Print out salary groups (individual list of values without applying the 
# final aggregation) grouped by middle initial. That is, for each unique middle initial, 
# print all of the salaries in that group.
 
middleinitialsalarygroup = defaultdict(list)


for ei in range(len(employeedf)): 
    middleinitialsalarygroup[employeedf['Middle'][ei]].append(employeedf['Salary'][ei])


for key, value in middleinitialsalarygroup.items():
    print(key, value)
    
    
    
    
    