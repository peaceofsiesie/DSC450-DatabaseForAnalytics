/*
	company.sql
	Alexander Rasin (with thanks to Eric J. Schwabe)
	CSC 455 Fall 2016

*/

-- drop tables

DROP TABLE EMPLOYEE CASCADE CONSTRAINTS;
DROP TABLE DEPARTMENT CASCADE CONSTRAINTS;
DROP TABLE PROJECT CASCADE CONSTRAINTS;
DROP TABLE WORKS_ON CASCADE CONSTRAINTS;

-- create and populate tables

CREATE TABLE EMPLOYEE
(
	Fname		VARCHAR(20),
	Minit		CHAR(1),
	Lname		VARCHAR(20),
	Ssn		CHAR(9),
	Bdate		DATE,
	Address		VARCHAR(30),
	Sex		CHAR(1),
	Salary		NUMBER(5),
	Super_Ssn	CHAR(9),
	Dno		NUMBER(1),

	PRIMARY KEY (Ssn),
		
	FOREIGN KEY (Super_ssn)
		REFERENCES EMPLOYEE (Ssn)
);

INSERT INTO EMPLOYEE VALUES ('James', 'E', 'Borg', '888665555', DATE '1937-11-10', '450 Stone, Houston, TX', 'M', 55000, NULL, 1);
INSERT INTO EMPLOYEE VALUES ('Jennifer', 'S', 'Wallace', '987654321', DATE '1941-06-20', '291 Berry, Bellaire, Tx', 'F', 37000, '888665555', 4);
INSERT INTO EMPLOYEE VALUES ('Franklin', 'T', 'Wong', '333445555', DATE '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5);
INSERT INTO EMPLOYEE VALUES ('John', 'B', 'Smith', '123456789', DATE '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Alicia', 'J', 'Zelaya', '999887777', DATE '1968-01-19', '3321 castle, Spring, TX', 'F', 25000, '987654321', 4);
INSERT INTO EMPLOYEE VALUES ('Ramesh', 'K', 'Narayan', '666884444', DATE '1920-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Joyce', 'A', 'English', '453453453', DATE '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Ahmad', 'V', 'Jabbar', '987987987', DATE '1969-03-29', '980 Dallas, Houston, TX', 'M', 22000, '987654321', 4);
INSERT INTO EMPLOYEE VALUES ('Melissa', 'M', 'Jones', '808080808', DATE '1970-07-10', '1001 Western, Houston, TX', 'F', 27500, '333445555', 5);

CREATE TABLE DEPARTMENT
(
	Dname		VARCHAR(20),
	Dnumber		NUMBER(1),
	Mgr_ssn		CHAR(9),
	Mgr_start_date	DATE,
	
	PRIMARY KEY (Dnumber),

	FOREIGN KEY (Mgr_ssn)
		REFERENCES EMPLOYEE (Ssn)
);

INSERT INTO DEPARTMENT VALUES ('Research', 5, '333445555', DATE '1988-05-22');
INSERT INTO DEPARTMENT VALUES ('Administration', 4, '987654321', DATE '1995-01-01');
INSERT INTO DEPARTMENT VALUES ('Headquarters', 1, '888665555', DATE '1981-06-19');

-- this alter is here because Employee table was created first

ALTER TABLE EMPLOYEE ADD FOREIGN KEY (Dno) REFERENCES DEPARTMENT (Dnumber);

CREATE TABLE PROJECT
(
	Pname		VARCHAR(20),
	Pnumber		NUMBER(2),
	Plocation	VARCHAR(20),
	Dnum		NUMBER(1),

	PRIMARY KEY (Pnumber)
);

INSERT INTO PROJECT VALUES ('ProductX', 1, 'Bellaire', 5);
INSERT INTO PROJECT VALUES ('ProductY', 2, 'Sugarland', 5);
INSERT INTO PROJECT VALUES ('ProductZ', 3, 'Houston', 5);
INSERT INTO PROJECT VALUES ('Computerization', 10, 'Stafford', 4);
INSERT INTO PROJECT VALUES ('Reorganization', 20, 'Houston', 1);
INSERT INTO PROJECT VALUES ('Newbenefits', 30, 'Stafford', 4);

CREATE TABLE WORKS_ON
(
	Essn		CHAR(9),
	Pno		NUMBER(2),
	Hours		NUMBER(3,1),
	
	PRIMARY KEY (Essn, Pno),

	FOREIGN KEY (Essn)
		REFERENCES EMPLOYEE (Ssn),

	FOREIGN KEY (Pno)
		REFERENCES PROJECT(Pnumber)
);

INSERT INTO WORKS_ON VALUES ('123456789', 1, 32.0);
INSERT INTO WORKS_ON VALUES ('123456789', 2, 8.0);
INSERT INTO WORKS_ON VALUES ('453453453', 1, 20.0);
INSERT INTO WORKS_ON VALUES ('453453453', 2, 20.0);
INSERT INTO WORKS_ON VALUES ('333445555', 1, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 2, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 3, 5.0);
INSERT INTO WORKS_ON VALUES ('333445555', 10, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 20, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 30, 5.0);
INSERT INTO WORKS_ON VALUES ('999887777', 30, 30.0);
INSERT INTO WORKS_ON VALUES ('999887777', 10, 10.0);
INSERT INTO WORKS_ON VALUES ('987987987', 10, 35.0);
INSERT INTO WORKS_ON VALUES ('987987987', 30, 5.0);
INSERT INTO WORKS_ON VALUES ('987654321', 30, 20.0);
INSERT INTO WORKS_ON VALUES ('987654321', 20, 15.0);
INSERT INTO WORKS_ON VALUES ('888665555', 20, 10.0);


-- display contents of tables

SELECT * FROM EMPLOYEE;
SELECT * FROM DEPARTMENT;
SELECT * FROM PROJECT;
SELECT * FROM WORKS_ON;



--1. Find the names of all employees who are directly supervised by 'Franklin T Wong' 
--(you cannot use Franklin’s SSN in the query, you can only use the name – one reason is that 
--SSN is sensitive information and we do not want SSN to appear in the query history log).

SELECT *
FROM Employee oe
WHERE EXISTS (  SELECT SSN
                FROM Employee
                WHERE FName = 'Franklin' AND oe.super_ssn = ssn);


--2. For each project, list the project name, project number, and the average hours 
-- per week (by all employees) spent on that project.

SELECT p.pname, p.pnumber, AVG(w.hours)
FROM PROJECT p
INNER JOIN WORKS_ON w
ON p.pnumber = w.pno
GROUP BY p.pname, p.pnumber 
ORDER BY p.pnumber ASC;

--3. For each department, retrieve the department name and the maximum salary of 
-- employees working in that department.  Order the output by department number in 
-- ascending order.

SELECT d.dname, d.dnumber, MAX(e.salary)
FROM Employee e, Department d
WHERE e.dno = d.dnumber
GROUP BY d.dname, d.dnumber
ORDER BY d.dnumber ASC

--4. Retrieve the average salary of all male employees.  

SELECT e.sex, AVG(e.salary)
FROM Employee e
WHERE e.sex = 'M'
GROUP BY e.sex;
                
--5. For each department whose average salary is greater than $34,000, 
-- retrieve the department name and the number of employees in that department.
            
SELECT d.dname, AVG(e.salary), count(e.ssn)
FROM Employee e, Department d
WHERE e.salary > 34000 AND e.dno = d.dnumber
GROUP BY d.dname

--6. Retrieve the names of employees whose salary is within $27,000 of the 
-- salary of the employee who is paid the most in the company 
-- (e.g., if the highest salary in the company is $87,000, retrieve the names of 
-- all employees that make at least $60,000.). 
-- Naturally, your query should work for any salary.

SELECT *
FROM Employee
WHERE salary < (SELECT Max(e.salary)
                 FROM Employee e) - 27000


--7. Find all female employees using:
--a. Plain SELECT query 

SELECT * 
FROM Employee e
WHERE e.sex = 'F';

--b. Sub-query

SELECT *
FROM Employee ei
WHERE EXISTS ( SELECT *
                FROM Employee eo
                WHERE ei.sex = eo.sex AND eo.sex = 'F');


--8. Find all employees who are not assigned to any project using a SET operation in SQL

SELECT * FROM Employee 
MINUS
SELECT DISTINCT e.fname, e.minit, e.lname, e.ssn, e.bdate, e.address, e.sex, e.salary, e.super_ssn, e.dno  
FROM Employee e, Works_On w
WHERE w.essn = e.ssn;