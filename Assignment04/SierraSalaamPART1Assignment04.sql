
-- Drop all the tables to clean up
DROP TABLE Handles;
DROP TABLE Animal;
DROP TABLE ZooKeeper;

CREATE TABLE ZooKeeper
(
  ZID        NUMBER(3,0),
  ZName       VARCHAR2(25) NOT NULL,
  HourlyRate NUMBER(6, 2) NOT NULL,
  
  CONSTRAINT ZooKeeper_PK
     PRIMARY KEY(ZID)
);


-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR(30) NOT NULL,
  ACategory VARCHAR(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


CREATE TABLE Handles
(
  ZooKeepID      NUMBER(3,0),
  AnimalID     NUMBER(3,0),
  
  Assigned     DATE,
  
  CONSTRAINT Handles_PK
    PRIMARY KEY(ZooKeepID, AnimalID),
    
  CONSTRAINT Handles_FK1
    FOREIGN KEY(ZooKeepID)
      REFERENCES ZooKeeper(ZID),
      
  CONSTRAINT Handles_FK2
    FOREIGN KEY(AnimalID)
      REFERENCES Animal(AID)
);


INSERT INTO ZooKeeper VALUES (1, 'Jim Carrey', 500);
INSERT INTO ZooKeeper VALUES (2, 'Tina Fey', 350);  
INSERT INTO ZooKeeper VALUES (3, 'Rob Schneider', 250);
  
INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);

INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);

INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.5);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.25);

INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);



INSERT INTO Handles VALUES(1, 1, '01-Jan-2000');
INSERT INTO Handles VALUES(1, 2, '02-Jan-2000');
INSERT INTO Handles VALUES(1, 10, '01-Jan-2000');

INSERT INTO Handles VALUES(2, 3, '02-Jan-2000');
INSERT INTO Handles VALUES(2, 4, '04-Jan-2000');
INSERT INTO Handles VALUES(2, 5, '03-Jan-2000');

INSERT INTO Handles VALUES(3, 7, '01-Jan-2000');
INSERT INTO Handles VALUES(3, 8, '03-Jan-2000');
INSERT INTO Handles VALUES(3, 9, '05-Jan-2000');
INSERT INTO Handles Values(3, 10,'04-Jan-2000');

--PART A

--Question 1
SELECT *
FROM Animal 
WHERE ACategory = 'rare'
ORDER BY TimeToFeed ASC;

--Question 2
SELECT aname, acategory
FROM Animal 
WHERE aname LIKE '%bear%';

--Question 3
SELECT aname
FROM Animal 
WHERE aname LIKE '%bear%' AND acategory = 'common';

--Question 4
SELECT aname
FROM Animal 
WHERE aname NOT LIKE '%tiger%';

--Question 5
SELECT h.zookeepid, a.aname
FROM Animal a, Handles h
WHERE a.aid = h.animalid;

--Question 6
SELECT a.aname, h.zookeepid
FROM Animal a
LEFT JOIN Handles h ON a.aid = h.animalid
ORDER BY a.aname;

--Question 7
SELECT z.zname, AVG(a.timetofeed)
FROM Animal a, Handles h, ZooKeeper z
WHERE a.aid = h.animalid AND z.zid = h.zookeepid
GROUP BY z.zname;

--Question 8
SELECT a.aname, z.zname, h.assigned
FROM Animal a, Handles h, ZooKeeper z
WHERE a.aid = h.animalid AND z.zid = h.zookeepid
ORDER BY h.assigned ASC;


