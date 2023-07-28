#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: July 30, 2023
Assignment 07
PART I

"""

import random as rm
import pandas as pd
import numpy as np

# PART I

# Question A

def generaterandomlist(x): 
    lst = []
    
    for i in range(x):
        num = rm.randint(27, 100)
        lst.append(num)
    
    return lst
    
# Question B

ranlstnum = generaterandomlist(90)
print(ranlstnum)
print("")
print("")

serlstrannum = pd.Series(ranlstnum)
print(serlstrannum)
print("")
print("")


count = 0 
i = 0

while i < len(serlstrannum):
    if serlstrannum[i] < 44:
        #print(i, serlstrannum[i])
        count += 1
    i += 1

print("Total Number of Numbers Less Than 44: ", count)
print("")
print("")
# Question C

arrrannum = np.array(ranlstnum)
arr = arrrannum.reshape(9,10)
print(arr)
print("")
print("")

for a in arr:
    for value in range(len(a)):
        if a[value] > 44:
            a[value] = 44
       
print(arr)


   









