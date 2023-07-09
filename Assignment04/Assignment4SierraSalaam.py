#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Sierra Salaam
Date: July 9, 2023
Assignment 04
File Saved Underneath File Path - '/Users/sierras/Documents/PythonProjects/School/DSC450/Homework4/Homework4SierraSalaam'
'''
import pandas as pd 
import re
import sqlite3



# PART I Question B

# Create Columns
animalcolumnnames = ['AID', 'AName', 'ACategory', 'TimetoFeed']

# Read File
animalfile = pd.read_csv("animal.txt", sep = ",", names = animalcolumnnames, skipinitialspace = True)

# Change To DF
animaldf = pd.DataFrame(data = animalfile)

#print the entire DF
print(animaldf)
print(" ")


# Question B Part 1

# Find the animal names and categories for animals not related to a tiger
print("Find the animal names and categories for animals not related to a tiger")
print("")
for i in range(len(animaldf)):
    if re.search('tiger*', animaldf['AName'][i]):
        pass
    else:
        print(animaldf['AName'][i], " ",  animaldf['ACategory'][i])

print(" ")


# Question B Part 2

# Find the names of the animals that are related to a bear and are not common
print("Find the names of the animals that are related to a bear and are not common")
print("")
for i in range(len(animaldf)):
    if re.search('bear*', animaldf['AName'][i]) and animaldf['ACategory'][i] != 'common':
        print(animaldf['AName'][i], " ",  animaldf['ACategory'][i])


# PART II Question B

# Create SQL Connection 
conn = sqlite3.connect('DSC450EJ.db')

# Create Table Statement

createJobDetailstbl = '''

CREATE TABLE JobDetails
(
  JName       VARCHAR2(50),
  JSalary     VARCHAR(30),
  JAssistant  VARCHAR(3),
  
    CONSTRAINT JobDetails_PK
        PRIMARY KEY(JName)
);

'''

createEmployertbl = '''
CREATE TABLE Employer
(
  EFirst    VARCHAR2(25),
  ELast     VARCHAR2(25),
  EAddress  VARCHAR2(150),
  EJob      VARCHAR2(50) NOT NULL,

  
  CONSTRAINT Employer_PK1
     PRIMARY KEY(EFirst, ELast, EJob),

    CONSTRAINT Employer_FK1
        FOREIGN KEY(EJob)
            REFERENCES JobDetails(JName)
);


'''

# Drop Table Statments
dropEmployertbl = "DROP TABLE Employer;"

dropJobDetailstbl = "DROP TABLE JobDetails;"


# View tables statments
viewJobDetailstbl = "SELECT * FROM JobDetails; "

viewEmployertbl = "SELECT * FROM Employer; "

# Insert statments
JobDetailsInsertStatement = "INSERT OR IGNORE INTO JobDetails VALUES (?, ?, ?);"

EmployerInsertStatment = "INSERT OR IGNORE INTO Employer VALUES (?, ?, ?, ?);"




# PART II Question C


eandjcolumnnames = ['First', 'Last', 'Address', 'Job', 'Salary', 'Assistant'] # Create column names

eandjfile = pd.read_csv("data_module4_part2.txt", sep = ",", names = eandjcolumnnames, skipinitialspace = True, keep_default_na = False) # Read File 

eandjdf = pd.DataFrame(data = eandjfile) # Establish DF

# Removing all NULL values from 1NF SQL Schema
for col in eandjdf: 
    for i in range(len(eandjdf.index.values)):  
        if eandjdf[col][i].strip() == 'NULL':
            eandjdf[col][i] = None



# Spliting up DFs to 3NF
employerdf = eandjdf.iloc[:,:4]
jobdf = eandjdf.iloc[:,3:]


# Openning connection
cursor = conn.cursor() 

# Drop Tables
cursor.execute(dropEmployertbl)
conn.commit()

cursor.execute(dropJobDetailstbl)
conn.commit()

# Create Tables
cursor.execute(createJobDetailstbl)   # create the JobDetails table
conn.commit()

cursor.execute(createEmployertbl)   # create the Employer table
conn.commit()


# Insert Values

for jvalue in jobdf.index:
    jinsertvalue = jobdf['Job'][jvalue], jobdf['Salary'][jvalue], jobdf['Assistant'][jvalue]
    cursor.execute(JobDetailsInsertStatement, (jinsertvalue))
    conn.commit()
    
for evalue in employerdf.index:
    einsertvalue = employerdf['First'][evalue], employerdf['Last'][evalue], employerdf['Address'][evalue], employerdf['Job'][evalue]
    cursor.execute(EmployerInsertStatment, (einsertvalue))
    conn.commit()


# View Tables and Values
cursor.execute(viewJobDetailstbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for JobDetails Table Entires")
print(cursor.fetchall())

cursor.execute(viewEmployertbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Employer Table Entires")
print(cursor.fetchall())
        


# PART II Question D 

# Finding all jobs with no salary 

JobNullSalary = "SELECT * FROM JobDetails WHERE JSalary IS NULL;"

print("")
print("Count All NULLS In Salary")
cursor.execute(JobNullSalary)
conn.commit()   # finalize inserted data
print(cursor.fetchall())

conn.close() # close the connection

