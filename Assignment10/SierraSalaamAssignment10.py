#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Sierra Salaam
Date: August 20, 2023
Assignment 10
filepath : /Users/sierras/Documents/PythonProjects/School/DSC450/Homework10-Final
"""

import urllib
from statistics import mean
import sqlite3
import re
import json
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

## PART I ##

##### connect to web and open link #####
webKD = urllib.request.urlopen('http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt')

##### Creating SQL Schema, Drop Tables, Create Tables and Execute/Commit To Changes #####

# Create SQL Connection 
conn = sqlite3.connect('DSC450FinalExam.db', isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)

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

# Insert Statements I
TWAInsertStatement = "INSERT OR IGNORE INTO TweetAttributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
UDInsertStatement = "INSERT OR IGNORE INTO UserAttributes VALUES (?, ?, ?, ?, ?);"
GLInsertStatement = "INSERT OR IGNORE INTO GeoAttributes VALUES (?, ?, ?, ?);"


# Insert Statements II

UD2InsertStatement = "INSERT OR IGNORE INTO UserAttributes (UserID, UserName, UserDescription, UserScreen_Name, UserFriends_Count) Values (?, ?, ?, ?, ?)"
TWA2InsertStatement = "INSERT OR IGNORE INTO TweetAttributes (IdStr, CreatedAt, TextDetail, SourceURL, Ref_UserID, IRTuser_id, IRTscreen_name, IRTstatus_id, Retweet_count, Contributors, Ref_GeoID) Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
GL2InsertStatement = "INSERT OR IGNORE INTO GeoAttributes (GeoID, GeoType, GeoLat, GeoLon) Values (?, ?, ?, ?)"



# Connection Object with Row Factory
conn.row_factory = sqlite3.Row


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



##### Question A - Use python to download tweets from the web and save to a local text file 
# (not into a database yet, just to a text file). This is as simple as it sounds, all you 
# need is a for-loop that reads lines from the web and writes them into a file.


tweetfile = open("TweetFileQuestion1A", "w")

count = 1 
for line in webKD: 
    if count < 650000:
        tweetfile.write(line.decode('UTF-8'))
        count += 1
        print(count)
    else:
        tweetfile.close()  
        break
    
    
tweetfile.close()



##### Question B - b.	Repeat what you did in part 1-a, but instead of saving tweets to 
# the file, populate the 3-table schema that you previously created in SQLite. Be sure 
# to execute commit and verify that the data has been successfully loaded. Report loaded 
# row counts for each of the 3 tables.



count = 1

for line in webKD:
    if count < 650000: # 130000 tweets & 650000 tweets
        data = json.loads(line)
        
        
        if data['geo'] == None:
            glprimarykey = None
            pass
        else:
            glprimarykey = data['geo']['coordinates'][0] + data['geo']['coordinates'][1]
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
        
        count += 1
        print(count)
        
    else:
        break



###### Question C - Use your locally saved tweet file to repeat the database population 
# step from part-c. That is, load the tweets into the 3-table database using your saved 
# file with tweets. This is the same code as in 1-b, but reading tweets from your file, 
# not from the web.


savetweetfile = open("TweetFileQuestion1A", "r")


for stf in savetweetfile: 
    
    tweetdata = json.loads(stf)

    
    glprimarykey = None

    if tweetdata['geo'] == None:
        glprimarykey = None
        pass
    else:
        glprimarykey = tweetdata['geo']['coordinates'][0] + tweetdata['geo']['coordinates'][1]
        glvalue = glprimarykey, tweetdata['geo']['type'], tweetdata['geo']['coordinates'][0], tweetdata['geo']['coordinates'][1]
        cursor.execute(GLInsertStatement, (glvalue))
        conn.commit() 
        glprimarykey = glprimarykey + 1
     
        
    twavalue = tweetdata['id_str'], tweetdata['created_at'], tweetdata['text'], tweetdata['source'],tweetdata['user']['id'], tweetdata['in_reply_to_user_id'], tweetdata['in_reply_to_screen_name'], tweetdata['in_reply_to_status_id'], tweetdata['retweet_count'], tweetdata['contributors'], glprimarykey 
    cursor.execute(TWAInsertStatement, (twavalue))
    conn.commit()
    
    udvalue = tweetdata['user']['id'], tweetdata['user']['name'], tweetdata['user']['description'], tweetdata['user']['screen_name'], tweetdata['user']['friends_count']
    cursor.execute(UDInsertStatement, (udvalue))
    conn.commit()


savetweetfile.close()




###### Question D - Repeat the same step with a batching size of 2,500 (i.e. by 
# inserting 2,500 rows at a time with executemany instead of doing individual inserts). 
# Since many of the tweets are missing a Geo location, its fine for the batches of Geo 
# inserts to be smaller than 2,500. 

# Insert Statements



glprimarykey = None

useridlst = []
tweetlst = []
gllst = []


savetweetfile = open("TweetFileQuestion1A", "r")


for stf in savetweetfile:
    
    tweetdata = json.loads(stf)
    
    udtemp = []
    tweettemp = []
    gltemp = []
    
    if len(tweetlst) < 650000: 
        udtemp.append(tweetdata['user']['id'])
        udtemp.append(tweetdata['user']['name'])
        udtemp.append(tweetdata['user']['description'])
        udtemp.append(tweetdata['user']['screen_name'])
        udtemp.append(tweetdata['user']['friends_count'])
        
        useridlst.append(udtemp)
  
        tweettemp.append(tweetdata['id_str'])
        tweettemp.append(tweetdata['created_at'])
        tweettemp.append(tweetdata['text']) 
        tweettemp.append(tweetdata['source']) 
        tweettemp.append(tweetdata['user']['id'])
        tweettemp.append(tweetdata['in_reply_to_user_id'])
        tweettemp.append(tweetdata['in_reply_to_screen_name'])
        tweettemp.append(tweetdata['in_reply_to_status_id'])
        tweettemp.append(tweetdata['retweet_count'])
        tweettemp.append(tweetdata['contributors'])
        tweettemp.append(glprimarykey) 
        
        tweetlst.append(tweettemp)
      
        
        if tweetdata['geo'] == None:
            glprimarykey = None
            pass
        else:
            glprimarykey = tweetdata['geo']['coordinates'][0] + tweetdata['geo']['coordinates'][1]
            gltemp.append(glprimarykey)
            gltemp.append(tweetdata['geo']['type'])
            gltemp.append(tweetdata['geo']['coordinates'][0])
            gltemp.append(tweetdata['geo']['coordinates'][1])
            
            gllst.append(gltemp)
            
        print(len(tweetlst))
        
    else:
        savetweetfile.close()
        break

cursor.executemany(UD2InsertStatement, (useridlst))
conn.commit()

cursor.executemany(TWA2InsertStatement, (tweetlst))
conn.commit()

cursor.executemany(GL2InsertStatement, (gllst))
conn.commit()


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




###### Question E - e.	Plot the resulting runtimes (# of tweets versus runtimes) 
# using matplotlib for 1-a, 1-b, 1-c, and 1-d. How does the runtime compare?


xlst = ['1a', '1b', '1c', '1d']
ylst130 = [58,144,136,6]
ylst650 = [300, 703, 691,35]


fig = plt.figure()
fig.set_size_inches(15,10)

sp = fig.add_subplot(2,3,3)

sp.scatter(xlst, ylst130, color = 'r', label = '130000 Tweets' )
sp.scatter(xlst, ylst650, color = 'b', label = '650000 Tweets' )

plt.ylabel("Runtime Performance (Seconds)")
plt.xlabel("Task When Runtime Was Performed")

fig.legend(loc="right")

plt.show()


## PART II ##


##### Question A - Write and execute a SQL query to find the average latitude 
# value for each user ID, using both AVG and SUM/COUNT. This query does not 
# need the User table because User ID is a foreign key in the Tweet table. 
# E.g., something like SELECT UserID, AVG(latitude), SUM(latitude)/COUNT(latitude) 
# FROM Tweet, Geo WHERE Tweet.GeoFK = Geo.GeoID GROUP BY UserID;


AvgLat = '''
SELECT T.Ref_UserID, AVG(G.GeoLat), SUM(G.GeoLat)/COUNT(G.GeoLat) 
FROM TweetAttributes As T, GeoAttributes As G
WHERE T.Ref_GeoID  = G.GeoID 
GROUP BY T.Ref_UserID;

'''


# View Tables and Values
cursor.execute(AvgLat)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Query For Average Latitude")
print(cursor.fetchall())




##### Question B - Re-execute the SQL query in part 2-a 5 times and 20 times and
# measure the total runtime (just re-run the same exact query multiple times using 
# a for-loop, it is as simple as it looks). Does the runtime scale linearly? (i.e., 
# does it take 5X and 20X as much time?)


for i in range(5):
    print(i)
    cursor.execute(AvgLat)
    conn.commit()   # finalize inserted data
    print(" ")
    print("SQL Query For Average Latitude")
    print(cursor.fetchall())
    



##### Question C - c.	Write the equivalent of the 2-a query in python 
# (without using SQL) by reading it from the file with 650,000 tweets.


savetweet = open("TweetFileQuestion1A", "r")

tweetdic = {}

for st in savetweet:
    
    datatweet = json.loads(st)
    
    if datatweet['user']['id'] in tweetdic and datatweet['geo'] != None :
        tweetdic.setdefault(datatweet['user']['id']).extend([datatweet['geo']['coordinates'][0]])
        break
    elif datatweet['user']['id'] not in tweetdic and datatweet['geo'] != None:
        tweetdic[datatweet['user']['id']] = [datatweet['geo']['coordinates'][0]]
    else:
        pass
        
savetweet.close()

print(tweetdic)

for k, v in tweetdic.items():
    calulateavg = sum(v)/len(v)
    print(k, mean(v), calulateavg)
    



##### Question D - Re-execute the query in part 2-c 5 times and 20 times and measure 
# the total runtime. Does the runtime scale linearly? 

savetweet = open("TweetFileQuestion1A", "r")

for i in range(21):
    
    tweetdic = {}

    for st in savetweet:
    
        datatweet = json.loads(st)
    
        if datatweet['user']['id'] in tweetdic and datatweet['geo'] != None :
            tweetdic.setdefault(datatweet['user']['id']).extend([datatweet['geo']['coordinates'][0]])
            break
        elif datatweet['user']['id'] not in tweetdic and datatweet['geo'] != None:
            tweetdic[datatweet['user']['id']] = [datatweet['geo']['coordinates'][0]]
        else:
            pass
        
    
    for k, v in tweetdic.items():
        calulateavg = sum(v)/len(v)
        print(k, mean(v), calulateavg)
        
    print(i)
    
savetweet.close()

##### Question E - Write the equivalent of the 2-a query in python by using 
# regular expressions instead of json.loads(). Do not use json.loads() here. 
# Note that you only need to find userid and geo location (if any) for each tweet, 
# you don’t need to parse the whole thing.

savetweetreg = open("TweetFileQuestion1A", "r")

tweetdic = {}

for strg in savetweetreg:
    attributelength = len(strg)
    
    startuserid = re.search('{"id":',strg).end()
    #print(startuserid)
    
    for i in range(startuserid,attributelength):
        if strg[i] == ",":
            userid = strg[startuserid:i]
            userid = int(userid)
            break
        
    #print(userid)


    startlatcoor = re.search('"coordinates":',strg).end()
    #print(startlatcoor)
    
    for i in range(startlatcoor,attributelength):
        if strg[i] == ",":
            geolat = strg[startlatcoor:i]
            break
        
    
    
    if geolat == 'null':
        pass
    else:
        geolat = strg[startlatcoor+1:i]
        geolat = float(geolat)
        #print(geolat)
        if userid in tweetdic:
            tweetdic.setdefault(userid).append(geolat)
            break
        elif userid not in tweetdic:
            tweetdic[userid] = [geolat]
        else:
            pass
        
            
savetweetreg.close()

print(tweetdic)

for k, v in tweetdic.items():
    calulateavg = sum(v)/len(v)
    print(k, mean(v), calulateavg)
        
   

##### Question F - Re-execute the query in part 2-e 5 times and 20 times and 
# measure the total runtime. Does the runtime scale linearly? 

savetweetreg = open("TweetFileQuestion1A", "r")


for count in range(21):
    
    tweetdic = {}

    for strg in savetweetreg:
        attributelength = len(strg)
        
        startuserid = re.search('{"id":',strg).end()
        #print(startuserid)
        
        for i in range(startuserid,attributelength):
            if strg[i] == ",":
                userid = strg[startuserid:i]
                userid = int(userid)
                break
            
        #print(userid)


        startlatcoor = re.search('"coordinates":',strg).end()
        #print(startlatcoor)
        
        for i in range(startlatcoor,attributelength):
            if strg[i] == ",":
                geolat = strg[startlatcoor:i]
                break
            
        
        
        if geolat == 'null':
            pass
        else:
            geolat = strg[startlatcoor+1:i]
            geolat = float(geolat)
            #print(geolat)
            if userid in tweetdic:
                tweetdic.setdefault(userid).append(geolat)
                break
            elif userid not in tweetdic:
                tweetdic[userid] = [geolat]
            else:
                pass
            
                


    print(tweetdic)

    for k, v in tweetdic.items():
        calulateavg = sum(v)/len(v)
        print(k, mean(v), calulateavg)
        
    print(count)

savetweetreg.close()   


## PART III ##

##### Question A - Using the database with 650,000 tweets, create a new table 
# that corresponds to the join of all 3 tables in your database, including records 
# without a geo location. This is the equivalent of a materialized view but since 
# SQLite does not support MVs, we will use CREATE TABLE AS SELECT (instead of CREATE 
# MATERIALIZED VIEW AS SELECT).


glprimarykey = None

useridlst = []
tweetlst = []
gllst = []


savetweetfile = open("TweetFileQuestion1A", "r")


for stf in savetweetfile:
    
    tweetdata = json.loads(stf)
    
    udtemp = []
    tweettemp = []
    gltemp = []
    
    if len(tweetlst) < 650001: 
        udtemp.append(tweetdata['user']['id'])
        udtemp.append(tweetdata['user']['name'])
        udtemp.append(tweetdata['user']['description'])
        udtemp.append(tweetdata['user']['screen_name'])
        udtemp.append(tweetdata['user']['friends_count'])
        
        useridlst.append(udtemp)
  
        tweettemp.append(tweetdata['id_str'])
        tweettemp.append(tweetdata['created_at'])
        tweettemp.append(tweetdata['text']) 
        tweettemp.append(tweetdata['source']) 
        tweettemp.append(tweetdata['user']['id'])
        tweettemp.append(tweetdata['in_reply_to_user_id'])
        tweettemp.append(tweetdata['in_reply_to_screen_name'])
        tweettemp.append(tweetdata['in_reply_to_status_id'])
        tweettemp.append(tweetdata['retweet_count'])
        tweettemp.append(tweetdata['contributors'])
        tweettemp.append(glprimarykey) 
        
        tweetlst.append(tweettemp)
      
        
        if tweetdata['geo'] == None:
            glprimarykey = None
            gltemp.append(glprimarykey)
            gltemp.append(None)
            gltemp.append(None)
            gltemp.append(None)
            pass
        else:
            glprimarykey = tweetdata['geo']['coordinates'][0] + tweetdata['geo']['coordinates'][1]
            gltemp.append(glprimarykey)
            gltemp.append(tweetdata['geo']['type'])
            gltemp.append(tweetdata['geo']['coordinates'][0])
            gltemp.append(tweetdata['geo']['coordinates'][1])
            
            gllst.append(gltemp)
            
        print(len(tweetlst))
        
    else:
        savetweetfile.close()
        break

cursor.executemany(UD2InsertStatement, (useridlst))
conn.commit()

cursor.executemany(TWA2InsertStatement, (tweetlst))
conn.commit()

cursor.executemany(GL2InsertStatement, (gllst))
conn.commit()



AlltableMatView = '''

CREATE TABLE AllTableMatView AS
    SELECT T.IdStr, T.CreatedAt, T.TextDetail, T.SourceURL	, T.Ref_UserID, T.IRTuser_id, T.IRTscreen_name, T.IRTstatus_id, T.Retweet_count, T.Contributors, T.Ref_GeoID, U.UserName, U.UserDescription, U.UserScreen_Name, U.UserFriends_Count, G.GeoType, G.GeoLat, G.GeoLon
    FROM TweetAttributes As T 
    JOIN UserAttributes As U 
        ON T.Ref_UserID = U.UserID
    JOIN GeoAttributes As G 
        ON T.Ref_GeoID = G.GeoID; 

'''

DropAllTabMatView = 'DROP TABLE AllTableMatView;'


cursor.execute(DropAllTabMatView)
conn.commit()


cursor.execute(AlltableMatView)
conn.commit()


ReviewJoinTables = "SELECT * FROM AllTableMatView"



# View Tables and Values
cursor.execute(ReviewJoinTables)
conn.commit()   # finalize inserted data
print(" ")
print("SQL Schema for All Table Entires")
print(cursor.fetchall())





##### Question B - b.	Export the contents of 1) the Tweet table and 2) your new table 
# from 3-a into a new JSON file (i.e., create your own JSON file with just the keys you 
# extracted). You do not need to replicate the structure of the input and can come up 
# with any reasonable keys for each field stored in JSON structure (e.g., you can have 
# longitude as “longitude” key when the location is available). 
# How do the file sizes compare to the original input file?



newfiletweet = open("TweetFileQuestion3B", "w")

cursor.execute(ReviewJoinTables)
conn.commit()
resultJoinTable = [dict(rowjt) for rowjt in cursor.fetchall()]

cursor.execute(viewTWAtbl)
conn.commit()
resultTweetAttributes = [dict(rowta) for rowta in cursor.fetchall()]

allresults = resultJoinTable, resultTweetAttributes


newfiletweet.write(json.dumps(allresults))


newfiletweet.close()



##### Question C - c.	Export the contents of 1) the Tweet table and 2) your table 
# from 3-a into a .csv (comma separated value) file. How do the file size compare 
# to the original input file and to the files in 3-b?

CombineTMVandTWA = '''

    SELECT A.IdStr, A.CreatedAt, A.TextDetail, A.SourceURL	, A.Ref_UserID, A.IRTuser_id, A.IRTscreen_name, A.IRTstatus_id, A.Retweet_count, A.Contributors, A.Ref_GeoID, A.UserName, A.UserDescription, A.UserScreen_Name, A.UserFriends_Count, A.GeoType, A.GeoLat, A.GeoLon
    FROM AlltableMatView As A  
    UNION ALL
    SELECT T.IdStr, T.CreatedAt, T.TextDetail, T.SourceURL	, T.Ref_UserID, T.IRTuser_id, T.IRTscreen_name, T.IRTstatus_id, T.Retweet_count, T.Contributors, T.Ref_GeoID, NULL, NULL, NULL, NULL, NULL, NULL, NULL
    FROM TweetAttributes As T
'''


cursor.execute(CombineTMVandTWA)
conn.commit()


tweetfilecsv = pd.read_sql_query(CombineTMVandTWA, conn)
tweetfilecsv.to_csv('TweetFileQuestion3C.csv', index=False)


conn.close() # close the connection


