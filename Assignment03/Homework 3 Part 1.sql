-- Drop all the tables to clean up
DROP TABLE Handles;
DROP TABLE Animal;


-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName     VARCHAR2(32) NOT NULL,
  ACategory VARCHAR2(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.6);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.75);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.5);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.5);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.75);
INSERT INTO Animal VALUES(11,'Llama', NULL, 3.5);


-- Find all the animals (their names) that take less than 2 hours to feed

SELECT AName, timetofeed 
    FROM animal
    WHERE timetofeed < 2; 


-- Find both the rare and exotic animals (in a single query, not two different queries)
SELECT AName, ACategory 
    From Animal
    WHERE ACategory = 'rare' OR ACategory = 'exotic';


-- Return the listings for all animals whose rarity is missing (NULL) in the database
SELECT AName, ACategory 
    FROM Animal
    WHERE ACategory IS NULL;

-- Find the rarity rating of all animals that require between 1.5 and 2.5 hours to be fed
SELECT AName, timetofeed 
    FROM Animal
    WHERE timetofeed >= 1.5 AND timetofeed <= 2.5;

-- Find the minimum and maximum feeding time amongst all the animals in the zoo (in a single SQL query, not two different queries)
SELECT MIN(timetofeed) AS MinTime, MAX(timetofeed) AS MaxTime
    FROM Animal;
  
-- Find the average feeding time for all of the common animals
SELECT AVG(timetofeed) AS AverageTime
    FROM Animal;
    
-- Determine how many NULLs there are in the ACategory column using SQL
SELECT Count(*)
    FROM Animal
    WHERE ACategory IS NULL;


-- Find all animals named 'Alpaca', 'Llama' or any other animals that are not listed as exotic 
SELECT AName
    FROM Animal
    WHERE ACategory != 'exotic' OR ACategory IS NULL;