'''

Name: Sierra Salaam
Date: July 16, 2023
Assignment 05 PART 3
File Saved Underneath File Path - Users/sierras/Documents/PythonProjects/School/DSC450/Homework5/

'''

import sqlite3
import json


# PART III Question

# Create SQL Connection 
conn = sqlite3.connect('DSC450EJ.db')

# Create Table Statement

createTWAtbl = '''

CREATE TABLE TweetAttributes
(
	IdStr       NUMBER(30),
    CreatedAt	DATE,
	TextDetail	VARCHAR(255),
	SourceURL	VARCHAR(255),
	IRTuser_id	NUMBER(30),
	IRTscreen_name		VARCHAR(50),
	IRTstatus_id		NUMBER(30),
	Retweet_count		NUMBER(4),
	Contributors	    VARCHAR(30),

	PRIMARY KEY (IdStr)
		
);

'''


# Drop Table Statements
dropTWAtbl = "DROP TABLE TweetAttributes;"

# View Tables Statements
viewTWAtbl = "SELECT * FROM TweetAttributes; "

# View Count Of Rows Statements (confirm number of time "EndOfTweet" repeats is 182)
viewRowCountTWAtbl = "SELECT Count(*) FROM TweetAttributes; "

# View Count Of Null Values In IRTscreen_name Field
viewNullScreenNameTWAtbl = "SELECT Count(*) FROM TweetAttributes WHERE IRTscreen_name  IS NULL; "

# Insert Statements
TWAInsertStatement = "INSERT OR IGNORE INTO TweetAttributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"



# Read File 
fileinput = "Module5.txt"

f = open(fileinput, "r")
lines = f.read()
f.close()


# Openning connection
cursor = conn.cursor() 

# Drop Tables
cursor.execute(dropTWAtbl)
conn.commit()


# Create Tables
cursor.execute(createTWAtbl)   # create the JobDetails table
conn.commit()



# Loop through each line, create a dictionary and add fields to sql table

for l in lines.split("EndOfTweet"):
    data = json.loads(l) #loads when you convert a string and add the dictionary one at a time
    
    twavalue = data['id_str'], data['created_at'], data['text'], data['source'], data['in_reply_to_user_id'], data['in_reply_to_screen_name'], data['in_reply_to_status_id'], data['retweet_count'], data['contributors']
    cursor.execute(TWAInsertStatement, (twavalue))
    conn.commit()
    
# View Tables and Values
cursor.execute(viewTWAtbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for TweetAttributes Table Entires")
print(cursor.fetchall())

# Generate Count of Rows
cursor.execute(viewRowCountTWAtbl)
conn.commit()   # finalize inserted data
print(" ")
print("Count of Number Of Rows")
print(cursor.fetchall())

# Generate Count of Null Values In IRTscreen_name Field
cursor.execute(viewNullScreenNameTWAtbl)
conn.commit()   # finalize inserted data
print(" ")
print("Count of Null Values In IRTscreen_name Field")
print(cursor.fetchall())


conn.close() # close the connection