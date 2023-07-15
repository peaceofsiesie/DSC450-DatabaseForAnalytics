-- drop tables
DROP TABLE TWEET;

-- create and populate tables

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
 