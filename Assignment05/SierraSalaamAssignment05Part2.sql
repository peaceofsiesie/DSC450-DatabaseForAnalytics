-- drop tables
DROP TABLE CHAUFFEUR;

-- create and populate tables

CREATE TABLE CHAUFFEUR
(
	LNumber		NUMBER(10),
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