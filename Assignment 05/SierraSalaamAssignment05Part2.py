'''

Name: Sierra Salaam
Date: July 16, 2023
Assignment 05 PART 2
File Saved Underneath File Path - Users/sierras/Documents/PythonProjects/School/DSC450/Homework5/

'''


import pandas as pd
import sqlite3


# PART II

# Read and Create DataFrame

pcsfile = pd.read_csv("/Users/sierras/Documents/PythonProjects/School/DSC450/Homework5/SierraSalaamHomework5/Public_Chauffeurs_Short_hw3.csv", sep = ",", skipinitialspace = True, keep_default_na = False)

dfpcs = pd.DataFrame(data = pcsfile)


# print(pcsfile)

# Removing all NULL values from 1NF SQL Schema
for col in dfpcs: 
    for i in range(len(dfpcs.index.values)):  
        if dfpcs[col][i] == 'NULL' or dfpcs[col][i] == '':
            dfpcs[col][i] = None
            
print(dfpcs)

# Printing column name in Data Frame

'''
for col in dfpcs.columns:
    print(col)
'''

# Create SQL Connection 
conn = sqlite3.connect('DSC450Assignment5PARTII.db')

# Create Table Statement

createPCStbl = '''

CREATE TABLE Chauffeur
(
	LNumber		VARCHAR(20),
	LRenewed    DATE,
	LStatus		VARCHAR(10),
	LStatusDate		DATE,
	DriverType	VARCHAR(20),
	LType		VARCHAR(10),
	OriginalIssueDate		DATE,
	CName		VARCHAR(100),
	CSex	    VARCHAR(10),
	CCity		VARCHAR(100),
    CState	    CHAR(2),
    CRecordNumber CHAR(12),

	PRIMARY KEY (LNumber)
		
);

'''

# Drop Table Statements
dropPCStbl = "DROP TABLE Chauffeur;"

# View tables Statements
viewPCStbl = "SELECT * FROM Chauffeur; "

# Insert Statements
PCSInsertStatement = "INSERT OR IGNORE INTO Chauffeur VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

#Query Results
PCSNumRecords = "SELECT Count(*) FROM Chauffeur;"
PCSOriginalDateNull = "SELECT Count(LNumber) From Chauffeur WHERE OriginalIssueDate IS NULL;"

# Openning connection
cursor = conn.cursor() 

# Drop Tables
cursor.execute(dropPCStbl)
conn.commit()


# Create Tables
cursor.execute(createPCStbl)   # create the JobDetails table
conn.commit()

# Insert Values To Table
#dfpcs.to_sql('Chauffeur', conn=cursor)

for value in dfpcs.index:
    insertvalue = int(dfpcs['License Number'][value]), dfpcs['Renewed'][value], dfpcs['Status'][value], dfpcs['Status Date'][value], dfpcs['Driver Type'][value], dfpcs['License Type'][value], dfpcs['Original Issue Date'][value], dfpcs['Name'][value], dfpcs['Sex'][value], dfpcs['Chauffeur City'][value], dfpcs['Chauffeur State'][value], dfpcs['Record Number'][value]  
    cursor.execute(PCSInsertStatement, (insertvalue))
    conn.commit()

# View Tables and Values
cursor.execute(viewPCStbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Chauffeur Table Entires")
print(cursor.fetchall())

# Question A - How many records are in the Chauffeurs table and 

cursor.execute(PCSNumRecords)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Chauffeur Table Entires")
print(cursor.fetchall())

# Question B - How many of the records are missing the “Original Issue Date” entry

cursor.execute(PCSOriginalDateNull)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Orginal Issue Date in Chauffeur Table Entires")
print(cursor.fetchall())
# close connection
conn.close()
