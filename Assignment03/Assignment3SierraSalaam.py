'''
Name: Sierra Salaam
Date: July 2, 2023
Assignment 03

'''

import sqlite3

conn = sqlite3.connect('dsc450.db') # establishing connection

# Create Table. Sample Table Given - SQLite_LoadAnimalTable.py

createtbl = """
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),

  TimeToFeed NUMBER(4,2),

  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);

"""

# different SQL commands to call

droptbl = "DROP TABLE Animal;"

inserts = ["INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);", "INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);", "INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);", "INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);", "INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);", "INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);", "INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);", "INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);", "INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);", "INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);", "INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);"]

viewtable = "SELECT * FROM Animal;"

numberrows = "SELECT COUNT(*) FROM Animal;"

insertstatment = "INSERT INTO Animal VALUES (?, ?, ?, ?);"


'''
# Question A - Write python code that is going to export a table 
# from a SQLite database into a CSV file


cursor = conn.cursor()
#cursor.execute(droptbl)
conn.commit()


cursor.execute(createtbl)   # create the Animal table
for ins in inserts:         # insert the rows
    cursor.execute(ins)

conn.commit()   # finalize inserted data


cursor.execute(viewtable)
conn.commit()   # finalize inserted data
print(cursor.fetchall())

conn.close()    # close the connection


newfile = open("animal.txt", "w") # create a new file and write in file

# directory where new file will be placed - 
# /Users/sierras/Documents/PythonProjects/School/DSC450/Homework3

word = "(" # note that this is the index number within each string

for i in inserts:
    indexword = i.find(word)

    tablevalue = i[indexword+1:-2].replace("'", "")

    newfile.write(tablevalue + "\n")
    
newfile.close()


'''
# Question B - Write python code that is going to load the comma-separated animal.txt 
# file you have created in part-a into the Animal table in SQLite database

# open file 
    
linestablevalue = []

oldfile = open("animal.txt", "r")

for line in oldfile.readlines():
    linestablevalue.append(line.splitlines())

oldfile.close()


# move over all values to new list to proceed with additional modifications
newlst = []

for values in linestablevalue:
    for v in values:
        v = v.split(",")
        newlst.append(v)
        
print(" ")     
print("With quotes around the list of values")
print(linestablevalue)

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
        if isint(nlvalue[nv]) == True:
            nlvalue[nv] = int(nlvalue[nv]) 
        elif isfloat(nlvalue[nv]) == True:  
            nlvalue[nv] = float(nlvalue[nv])
  
print(" ")
print("quotes around the strings only")
print(newlst)
       
# create function to load in the data to database 

def executemany(lst):
    
    cursor = conn.cursor() # openning connection

    cursor.execute(droptbl)
    conn.commit()


    cursor.execute(createtbl)   # create the Animal table
    conn.commit()


    for insertvalues in lst:
        cursor.execute(insertstatment, insertvalues)
        conn.commit()


    print("All Values In Table")
    cursor.execute(viewtable)
    conn.commit()   # finalize inserted data
    print(cursor.fetchall())
    print(" ")

    print("Count of Rows In Animal Table")
    cursor.execute(numberrows)
    conn.commit()   # finalize inserted data
    print(cursor.fetchall())

    conn.close() # close the connection


def main():
    'This function will execute the results from the program' #docstring
    executemany(newlst) #testing out function
 


#main() # calling the main function






