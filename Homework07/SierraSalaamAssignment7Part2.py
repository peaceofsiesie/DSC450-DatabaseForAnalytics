#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: July 30, 2023
Assignment 07
PART II

"""

import urllib
import sqlite3  
import json

# connect to web and open link
webKD = urllib.request.urlopen('https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt')

allTweets = webKD.readlines()



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
    Ref_UserID  NUMBER(10), 
	IRTuser_id	NUMBER(30),
	IRTscreen_name		VARCHAR(50),
	IRTstatus_id		NUMBER(30),
	Retweet_count		NUMBER(4),
	Contributors	    VARCHAR(30),

	PRIMARY KEY (IdStr),
    
     FOREIGN KEY (Ref_UserID)
		REFERENCES UserAttributes(UserID) 
		
);

'''

createUDtbl = '''

CREATE TABLE UserAttributes
(

    UserID              NUMBER(30),
    UserName            VARCHAR(30),
    UserDescription     VARCHAR(255),
    UserFriends_Count   NUMBER(10),
    
    PRIMARY KEY (UserID)
     
);

'''


# Drop Table Statements
dropTWAtbl = "DROP TABLE TweetAttributes;"
dropUDtbl = "DROP TABLE UserAttributes;"


# View Tables Statements by Counting All Rows
viewTWAtbl = "SELECT Count(*) FROM TweetAttributes;"
viewUDtbl = "SELECT Count(*) FROM UserAttributes;"

# Insert Statements
TWAInsertStatement = "INSERT OR IGNORE INTO TweetAttributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
UDInsertStatement = "INSERT OR IGNORE INTO UserAttributes VALUES (?, ?, ?, ?);"


# Reading the twitterfile


webFile = urllib.request.urlopen('https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt')
twitterLine = webFile.readline()


# Openning connection
cursor = conn.cursor() 



# Drop Tables

cursor.execute(dropUDtbl)
conn.commit() 

cursor.execute(dropTWAtbl)
conn.commit()


# Create Tables

cursor.execute(createUDtbl)  
conn.commit()


cursor.execute(createTWAtbl)  
conn.commit()

# Insert Values Into Tables OR Error File

f = open("Module7_errors.txt", "w")


for tweet in allTweets:
    try:
        data = json.loads(tweet.decode('utf8'))
        twavalue = data['id_str'], data['created_at'], data['text'], data['source'],data['user']['id'], data['in_reply_to_user_id'], data['in_reply_to_screen_name'], data['in_reply_to_status_id'], data['retweet_count'], data['contributors']
        cursor.execute(TWAInsertStatement, (twavalue))
        conn.commit()
        udvalue = data['user']['id'], data['user']['name'], data['user']['description'], data['user']['friends_count']
        cursor.execute(UDInsertStatement, (udvalue))
        conn.commit()
    except ValueError:
            f.write(str(tweet))
           
f.close()    



# View Tables and Values
cursor.execute(viewTWAtbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for TweetAttributes Table Entires - Count")
print(cursor.fetchall())

cursor.execute(viewUDtbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for UserAttributes Table Entires - Count")
print(cursor.fetchall())

# Generate Count of Rows



conn.close() # close the connection

