#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: July 23, 2023
MidTerm

"""

# ----  PART IIII



#import pandas as pd
import sqlite3
import statistics 


# Create SQL Connection 
conn = sqlite3.connect('SierraSalaamDSC450MidTerm.db')

# Create Table Statement

createStudenttbl = '''

CREATE TABLE Student
(
     SID VARCHAR2(5),
     SName VARCHAR2(255),
     SAddress VARCHAR2(255),
     SGradYear NUMBER(4),

    CONSTRAINT Student_PK
        PRIMARY KEY(SID)
		
);

'''

createCoursetbl = '''

CREATE TABLE Course
(
  CName VARCHAR2(100),
  CDepartment VARCHAR2(50),
  CCredits NUMBER(2),

  CONSTRAINT C_PK
     PRIMARY KEY(CName)
		
);

'''

createEnrolledtbl = '''

CREATE TABLE Enrolled
(
  CName VARCHAR2(100),
  StudentID VARCHAR2(5),
  CGrade VARCHAR2(5),
  
  CONSTRAINT Course_PK
     PRIMARY KEY(CName, StudentID),
     
  CONSTRAINT C_FK1
     FOREIGN KEY(CName)
        REFERENCES Course(CName),
        
  CONSTRAINT C_FK2
     FOREIGN KEY(StudentID)
        REFERENCES Student(SID)
		
);

'''

# Drop Table Statements
dropEnrolledtbl = "DROP TABLE Enrolled;"
dropCoursetbl = "DROP TABLE Course;"
dropStudenttbl = "DROP TABLE Student;"

# View Tables Statements
viewEnrolledtbl = "SELECT * FROM Enrolled; "
viewCoursetbl = "SELECT * FROM Course; "
viewStudenttbl = "SELECT * FROM Student; "

# Insert Statements
StudentIN1 = "INSERT INTO Student VALUES (12345, 'Paul James Keeper','358 South Lotus APT 3 Chicago IL 60644', 2025);"
StudentIN2 = "INSERT INTO Student VALUES (23456, 'Larry Montgomery Parker', '191 Elmside Benton Harbor MI 49022', 2023);"
StudentIN3 = "INSERT INTO Student VALUES (34567, 'Ana Summer Bummer','621 Lake Street Oak Park IL 60632', 2020);"
StudentIN4 = "INSERT INTO Student VALUES (45678, 'Mary Montgomery Yonkers','2450 South Central Chicago IL 60623', 2024);"
StudentIN5 = "INSERT INTO Student VALUES (56789, 'Pat Sparks Briggs','789 West Cicero Ave Chicago IL 65801', 2025);"


CourseIN1 = "INSERT INTO Course VALUES ('CSC211', 'Computer Science', 4);"
CourseIN2 = "INSERT INTO Course VALUES ('IT130', 'Information System', 2);"
CourseIN3 = "INSERT INTO Course VALUES ('CSC451', 'Computer Science', 4);"
CourseIN4 = "INSERT INTO Course VALUES ('CSC430', 'Computer Science', 4);"


EnrolledIN1 = "INSERT INTO Enrolled VALUES('CSC211', 12345, 'A+');"
EnrolledIN2 = "INSERT INTO Enrolled VALUES('CSC451', 12345, 'D-');"
EnrolledIN3 = "INSERT INTO Enrolled VALUES('IT130', 23456, 'B-');"
EnrolledIN4 = "INSERT INTO Enrolled VALUES('CSC211',34567, 'C+');"
EnrolledIN5 = "INSERT INTO Enrolled VALUES('IT130', 34567, ' A+');"
EnrolledIN6 = "INSERT INTO Enrolled VALUES('CSC451',34567, 'B-');"
EnrolledIN7 = "INSERT INTO Enrolled VALUES('IT130',45678, 'F+');"
EnrolledIN8 = "INSERT INTO Enrolled VALUES('CSC211',45678, 'A');"

# Add All Insert Values To A List

InsertValues =  [StudentIN1, StudentIN2, StudentIN3, StudentIN4, StudentIN5, CourseIN1, CourseIN2, CourseIN3, CourseIN4, EnrolledIN1, EnrolledIN2, EnrolledIN3, EnrolledIN4, EnrolledIN5, EnrolledIN6, EnrolledIN7, EnrolledIN8]



# Openning connection
cursor = conn.cursor() 


# Drop Tables ****************************************

cursor.execute(dropEnrolledtbl)
conn.commit()

cursor.execute(dropCoursetbl)
conn.commit()

cursor.execute(dropStudenttbl)
conn.commit()

# Create Tables
cursor.execute(createStudenttbl)  
conn.commit()

cursor.execute(createCoursetbl)   # create the JobDetails table
conn.commit()

cursor.execute(createEnrolledtbl)   # create the JobDetails table
conn.commit()

# Insert Values To Table

for value in InsertValues:
    cursor.execute(value)
    conn.commit()


# View Tables and Values

'''
cursor.execute(viewStudenttbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Student Table Entires")
print(cursor.fetchall())


cursor.execute(viewCoursetbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Course Table Entires")
print(cursor.fetchall())

cursor.execute(viewEnrolledtbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for Enrolled Table Entires")
print(cursor.fetchall())

'''


# ---------------- Question A --------------------


# Drop the Tables 
drop1NFtblview = "DROP VIEW StuEnrCor;"

# Create The Query To View Data
tblview1NF = '''
    CREATE VIEW StuEnrCor AS
    SELECT s.sid, s.SName, s.SAddress, s.SGradYear, e.cgrade, c.cname, c.cdepartment, c.ccredits 
    FROM Enrolled e
    FULL OUTER JOIN Course c
    ON e.CName = c.CName
    FULL OUTER JOIN Student s
    ON s.SID = e.studentid;

'''

# Create The Query To Execute Data
tblview1NFselect = "SELECT * FROM StuEnrCor"


# Drop File ******************************************
cursor.execute(drop1NFtblview)
conn.commit()   

# Create View 
cursor.execute(tblview1NF)
conn.commit() 

# View The Selected Tabe
cursor.execute(tblview1NFselect)
conn.commit()   # finalize inserted data


lstvalues = []

for row in cursor.execute(tblview1NFselect):
    lstvalues.append(list(row))
  
# ---------------- Question B ---------------- 

outfile = open("output.txt", 'w+')

for l in range(len(lstvalues)):
    for v in range(len(lstvalues[l])):
        if lstvalues[l][v] == None:
            lstvalues[l][v] = 'NULL'
        lstvalues[l][v] = str(lstvalues[l][v])
        lstvalues[l][v] = str(lstvalues[l][v].replace("'", ""))
        
        valnum = lstvalues[l][v].isnumeric()
        
        if valnum == True:
            lstvalues[l][v] = int(lstvalues[l][v])
    
    lstvalues[l] = str(lstvalues[l])
    lstvalues[l] = lstvalues[l].replace("[", "")
    lstvalues[l] = lstvalues[l].replace("]", "\n")
    outfile.write(lstvalues[l])
     


# ----------------  Question C ---------------- 

InvaildEntry = "45678, 'Mary Montgomery Yonkers', '2450 South Central Chicago IL 60623', 2025, 'A', 'CSC451', 'Computer Science', 8"

outfile.write(InvaildEntry)

outfile.close()


# ---------------- Question D ---------------- 

linetblvalue = []
    
oldfile = open("output.txt", "r")

for line in oldfile.readlines():
    linetblvalue.append(line.splitlines())

oldfile.close()
   

newlst = []

for values in linetblvalue:
    for v in values:
        v = v.split(",")
        newlst.append(v)


# create functions to check values are integer or float
def isint(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
         return True
     
def isfloat(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
         return True
             
# modify the new list with proper value type within list 

for nlvalue in newlst: # looping through the list of value list
    for nv in range(len(nlvalue)): #looping through the values
        nlvalue[nv] = nlvalue[nv].strip() # making values into a list and remove grouped string 
        nlvalue[nv] = nlvalue[nv].replace("'", "")
        if isint(nlvalue[nv]) == True:
            nlvalue[nv] = int(nlvalue[nv]) 
        elif isfloat(nlvalue[nv]) == True:  
            nlvalue[nv] = float(nlvalue[nv])
            
        
cleanlst = newlst


CNameCreditVaildation = {}


for cl in cleanlst:
    if cl[5] in CNameCreditVaildation.keys() and cl[7] != CNameCreditVaildation[cl[5]]:
        print("Invaid Entry", cl[5], cl[7])
        print("")
        print("CName Has Exisiting Credit \n", "CName: ", cl[5] ,"Credit: ", CNameCreditVaildation[cl[5]])
    else:
        CNameCreditVaildation[cl[5]] = cl[7]
    
print("")
print(CNameCreditVaildation)      

# ----------------  Question E ----------------

departlst = []
mamdic = {}

for h in range(len(cleanlst)): 
    departlst.append(cleanlst[h][6])
    

departlst = list(set(departlst))


def maxmidvalue (lstofvalue, lstofcolumns, dicmaxmid):
    
    templst = []
    
    for loc in lstofcolumns:
        for lov in lstofvalue:
            if loc == lov[6]:
                templst.append(lov[3])
        
        for t in templst:
            if isinstance(t, str):  
                templst.remove(t)
        
        dicmaxmid[loc] = list(set(templst))
    
    return dicmaxmid
        
    
print(maxmidvalue(cleanlst, departlst, mamdic))
print("")

for k, v in mamdic.items():
    print("Department: ", k, "\n", "Max Number - ", max(v),"\n", "Median Number -", statistics.median(v))
    print(" ")
   
   

# Close connection
conn.close()
