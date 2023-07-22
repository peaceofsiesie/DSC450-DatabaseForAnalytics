-- Drop Tables

DROP TABLE Enrolled;
DROP TABLE Student;
DROP TABLE Course;

-- Create Tables 

CREATE TABLE Student
(
  SID VARCHAR2(5),
  SName VARCHAR2(255),
  SAddress VARCHAR2(255),
  SGradYear NUMBER(4),
  
  CONSTRAINT Student_PK
     PRIMARY KEY(SID)
);

CREATE TABLE Course
(
  CName VARCHAR2(100),
  CDepartment VARCHAR2(50),
  CCredits NUMBER(2),

  CONSTRAINT C_PK
     PRIMARY KEY(CName)
     
);

CREATE TABLE Enrolled
(
  CName VARCHAR2(100),
  StudentID VARCHAR2(5),
  CGrade VARCHAR2(5),
  
  CONSTRAINT Course_PK
     PRIMARY KEY(CName, StudentID),
     
  CONSTRAINT C_FK1
     FOREIGN KEY(CName)
        REFERENCES Course(CName),
        
  CONSTRAINT C_FK2
     FOREIGN KEY(StudentID)
        REFERENCES Student(SID)
);



-- Insert Into Tables

INSERT INTO Student VALUES ('12345', 'Paul James Keeper','358 Sout Lotus APT 3 Chicago, IL 60644', 2025);
INSERT INTO Student VALUES ('23456', 'Larry Montgomery Parker', '191 Elmside, Benton Harbor, MI 49022', 2023);
INSERT INTO Student VALUES ('34567', 'Ana Summer Bummer','621 Lake Street, Oak Park, IL 60632', 2020);
INSERT INTO Student VALUES ('45678', 'Mary Montgomery Yonkers','2450 South Central, Chicago, IL 60623', 2024);
INSERT INTO Student VALUES ('56789', 'Pat Sparks Briggs','789 West Cicero Ave, Chicago, IL 65801', 2025);


INSERT INTO Course VALUES ('CSC211', 'Computer Science', 4);
INSERT INTO Course VALUES ('IT130', 'Information System', 2);
INSERT INTO Course VALUES ('CSC451', 'Computer Science', 4);
INSERT INTO Course VALUES ('CSC430', 'Computer Science', 4);


INSERT INTO Enrolled VALUES('CSC211','12345', 'A+');
INSERT INTO Enrolled VALUES('CSC451','12345', 'D-');


INSERT INTO Enrolled VALUES('IT130','23456', 'B-');

INSERT INTO Enrolled VALUES('CSC211','34567', 'C+');
INSERT INTO Enrolled VALUES('IT130','34567', 'A+');
INSERT INTO Enrolled VALUES('CSC451','34567', 'B-');

INSERT INTO Enrolled VALUES('IT130','45678', 'F+');
INSERT INTO Enrolled VALUES('CSC211', '45678', 'A');
--INSERT INTO Enrolled VALUES('CSC430', '45678', 'B');


-- Queries

SELECT * FROM Student;
SELECT * FROM Course;
SELECT * FROM Enrolled;



-- Part III 

--Q1
SELECT s.SID, s.SName, s.SGradYear
FROM Student s
WHERE s.SGradYear = (SELECT Max(SGradYear)
                     FROM Student);
       
--Q2                     
SELECT s.SName, e.CName
FROM Student s, Enrolled e
WHERE s.SID = e.StudentID AND s.SName LIKE '%Montgomery%';

--Q3
SELECT s.SName, e.CName, s.SGradyear
FROM Student s
FULL OUTER JOIN Enrolled e
ON s.SID = e.studentid 
WHERE e.CName IS NULL OR e.StudentID IN (SELECT en.Studentid
                       FROM Enrolled en
                       GROUP BY en.Studentid
                       HAVING Count(en.Studentid) = 1);
--Q4
UPDATE Student s
    SET s.SGradYear = s.SGradYear + 1
    WHERE s.SAddress LIKE '%Chicago%';
    
--Q5
ALTER TABLE Course
ADD Chair VARCHAR2(32);


-- PART IIII

DROP VIEW StuEnrCor;

CREATE VIEW StuEnrCor AS
SELECT s.sid, s.SName, s.SAddress, s.SGradYear, e.cgrade, c.cname, c.cdepartment, c.ccredits 
FROM Enrolled e
FULL OUTER JOIN Course c
ON e.CName = c.CName
FULL OUTER JOIN Student s
ON s.SID = e.studentid;

SELECT * FROM StuEnrCor;



DROP VIEW MaxMedianGY;


CREATE VIEW MaxMedianGY AS
SELECT c.cdepartment, MAX(s.SGradYear) maGY, MEDIAN(s.SGradYear) mdGY
FROM Enrolled e
FULL OUTER JOIN Course c
ON e.CName = c.CName
FULL OUTER JOIN Student s
ON s.SID = e.studentid
GROUP BY c.cdepartment;

--SELECT * FROM StuEnrCor
SELECT * FROM MaxMedianGY

 


	
