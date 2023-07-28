-- drop tables
DROP TABLE TweetAttributes;
DROP TABLE UserDictionary;
-- create and populate tables


CREATE TABLE UserDictionary
(

    UserID              NUMBER(30),
    UserName            VARCHAR(30),
    UserDescription     VARCHAR(255),
    UserFriends_Count   NUMBER(10),
    
    PRIMARY KEY (UserID)
     
);

CREATE TABLE TweetAttributes
(
	IdStr       NUMBER(30),
    CreatedAt	DATE,
	TextDetail	VARCHAR(255),
	SourceURL	VARCHAR(255),
    Ref_UserID  NUMBER(30),
	IRTuser_id	NUMBER(30),
	IRTscreen_name		VARCHAR(50),
	IRTstatus_id		NUMBER(30),
	Retweet_count		NUMBER(4),
	Contributors	    VARCHAR(30),

	PRIMARY KEY (IdStr),
    
     FOREIGN KEY (Ref_UserID)
		REFERENCES UserDictionary(UserID) 
		
);

 