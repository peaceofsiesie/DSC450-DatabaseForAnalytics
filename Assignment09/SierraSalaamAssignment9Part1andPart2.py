#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: August 13, 2023
Assignment 09
PART I and PART II
filepath : /Users/sierras/Documents/PythonProjects/School/DSC450/Homework9
"""

import urllib
import sqlite3 
import json
import numpy as np 
import matplotlib.pyplot as plt

# PART I 


# connect to web and open link
webKD = urllib.request.urlopen('https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt')

allTweets = webKD.readlines()


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
    Ref_GeoID       NUMBER(10),

	PRIMARY KEY (IdStr),
    
     FOREIGN KEY (Ref_UserID)
		REFERENCES UserAttributes(UserID),
        
    FOREIGN KEY (Ref_GeoID)
   		REFERENCES GeoAttributes(GeoID) 
		
);

'''

createUDtbl = '''

CREATE TABLE UserAttributes
(

    UserID              NUMBER(30),
    UserName            VARCHAR(30),
    UserDescription     VARCHAR(255),
    UserScreen_Name      VARCHAR(50),
    UserFriends_Count   NUMBER(10),
    
    PRIMARY KEY (UserID)
     
);

'''

createGLtbl = '''

CREATE TABLE GeoAttributes
(

    GeoID               NUMBER(10),
    GeoType             VARCHAR(30),
    GeoLat              DECIMAL(5,10),
    GeoLon              DECIMAL(5,10),
    
    PRIMARY KEY (GeoID)
     
);

'''


# Drop Table Statements
dropTWAtbl = "DROP TABLE TweetAttributes;"
dropUDtbl = "DROP TABLE UserAttributes;"
dropGLtbl = "DROP TABLE GeoAttributes;"


# View Tables Statements by Counting All Rows
viewTWAtbl = "SELECT Count(*) FROM TweetAttributes;"
viewUDtbl = "SELECT Count(*) FROM UserAttributes;"
viewGLtbl = "SELECT Count(*) FROM GeoAttributes;"

# Insert Statements
TWAInsertStatement = "INSERT OR IGNORE INTO TweetAttributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
UDInsertStatement = "INSERT OR IGNORE INTO UserAttributes VALUES (?, ?, ?, ?, ?);"
GLInsertStatement = "INSERT OR IGNORE INTO GeoAttributes VALUES (?, ?, ?, ?);"


# Reading the twitterfile


webFile = urllib.request.urlopen('https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt')
twitterLine = webFile.readline()


# Openning connection
cursor = conn.cursor() 



# Drop Tables

cursor.execute(dropGLtbl)
conn.commit() 

cursor.execute(dropUDtbl)
conn.commit() 

cursor.execute(dropTWAtbl)
conn.commit()


# Create Tables

cursor.execute(createGLtbl)  
conn.commit()


cursor.execute(createUDtbl)  
conn.commit()

cursor.execute(createTWAtbl)  
conn.commit()

# Insert Values Into Tables OR Error File

f = open("Module9_errors.txt", "w")

glprimarykey = 100
for tweet in allTweets:
    try:
        data = json.loads(tweet.decode('utf8'))
        
        
        if data['geo'] == None:
            pass
        else:
            glvalue = glprimarykey, data['geo']['type'], data['geo']['coordinates'][0], data['geo']['coordinates'][1]
            cursor.execute(GLInsertStatement, (glvalue))
            conn.commit() 
            glprimarykey = glprimarykey + 1
        
        udvalue = data['user']['id'], data['user']['name'], data['user']['description'], data['user']['screen_name'], data['user']['friends_count']
        cursor.execute(UDInsertStatement, (udvalue))
        conn.commit()
        
        
        twavalue = data['id_str'], data['created_at'], data['text'], data['source'],data['user']['id'], data['in_reply_to_user_id'], data['in_reply_to_screen_name'], data['in_reply_to_status_id'], data['retweet_count'], data['contributors'], glprimarykey 
        cursor.execute(TWAInsertStatement, (twavalue))
        conn.commit()

    except ValueError:
            f.write(str(tweet))
           
   



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

cursor.execute(viewGLtbl)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for GeoAttributes Table Entires - Count")
print(cursor.fetchall())

# Generate Queries 



##### Question A



UserID89OR78Count = "SELECT IdStr, TextDetail  FROM TweetAttributes AS U WHERE IdStr LIKE '%89%' OR IdStr LIKE '%78%';"


cursor.execute(UserID89OR78Count)
conn.commit()   # finalize inserted data
print(" ")
print("SQL - Find tweets where tweet id_str contains “89” or “78” anywhere in the column")
print(cursor.fetchall())




##### Question B
useridvalues = [],[]

for tweet in allTweets:
    try:
        data = json.loads(tweet.decode('utf8'))

        useridvalues[0].append(data['id_str'])
        useridvalues[1].append(data['text'])
        
        
    except ValueError:
            f.write(str(tweet))


EightyNine   = '89'
SeventyEight = '78' 
lstofud89or78 = [],[] 

for udv in range(len(useridvalues[0])):
    idstrvalue = str(useridvalues[0][udv])
    if EightyNine in idstrvalue:
        lstofud89or78[0].append(useridvalues[0][udv])
        lstofud89or78[1].append(useridvalues[1][udv])
    if SeventyEight in idstrvalue:
       lstofud89or78[0].append(useridvalues[0][udv])
       lstofud89or78[1].append(useridvalues[1][udv])

print("PYTHON - Find tweets where tweet id_str contains “89” or “78” anywhere in the column")
print(lstofud89or78)


##### Question C

UniqueFriendCount = "SELECT COUNT(DISTINCT U.UserFriends_Count) FROM UserAttributes AS U;"

cursor.execute(UniqueFriendCount)
conn.commit()   # finalize inserted data
print(" ")
print("SQL - Find how many unique values are there in the “friends_count” column")
print(cursor.fetchall())



##### Question D

friendcountvalues = []

for tweet in allTweets:
    try:
        data = json.loads(tweet.decode('utf8'))
        friendcountvalues.append(data['user']['friends_count'])
        
    except ValueError:
            f.write(str(tweet))
            
fcarray = np.array(friendcountvalues)
print(" PYTHON - Find how many unique values are there in the “friends_count” column")
print(len(np.unique(fcarray)))



##### Question E

tweetandusernamecount = [],[]


for tweet in allTweets:
    try:
        data = json.loads(tweet.decode('utf8'))
        if len(tweetandusernamecount[0]) == 60:
            break
        else:
            tweetandusernamecount[0].append(len(data['user']['name']))
            tweetandusernamecount[1].append(len(data['text']))
        
        
    except ValueError:
            f.write(str(tweet))


fig = plt.figure()
fig.set_size_inches(15,10)

sp = fig.add_subplot(2,2,2)

sp.scatter(tweetandusernamecount[0], tweetandusernamecount[0], color = 'r' )
sp.scatter(tweetandusernamecount[1], tweetandusernamecount[1], color = 'b' )

fig.savefig('PartIE.pdf', bbox_inches = 'tight')

f.close()



# PART II

##### Question A - Create an index on userid in Tweet table in SQLite (submit SQL code for this question). 


createuseridindex = "CREATE Index UserIDTweetsIndex ON TweetAttributes(Ref_UserID);"

cursor.execute(createuseridindex)
conn.commit()   


##### Question B - Create a composite index on (friends_count, screen_name) in User 


createuseridfsindex = "CREATE Index UserIDFSIndex ON UserAttributes(UserFriends_Count, UserScreen_Name);"

cursor.execute(createuseridfsindex)
conn.commit() 


##### Question C - Create a materialized view 

dropMTVUDContain8978tbl = "DROP TABLE MTVUDContain8978;"

createMTVUDContain8978tbl = "CREATE TABLE MTVUDContain8978 AS SELECT IdStr, TextDetail  FROM TweetAttributes AS U WHERE IdStr LIKE '%89%' OR IdStr LIKE '%78%';"

viewMTVUDContain8978tbl = "SELECT * FROM MTVUDContain8978;"

cursor.execute(dropMTVUDContain8978tbl)
conn.commit()   # finalize inserted data


cursor.execute(createMTVUDContain8978tbl)
conn.commit()   # finalize inserted data


cursor.execute(viewMTVUDContain8978tbl)
conn.commit() 
print(" ")
print("SQL - Find tweets where tweet id_str contains “89” or “78” anywhere in the column")
print(cursor.fetchall())



conn.close() # close the connection




