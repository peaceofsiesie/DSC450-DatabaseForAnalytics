DROP TABLE STUDENT CASCADE CONSTRAINTS;

CREATE TABLE STUDENT(
	ID		CHAR(3),
	Name		VARCHAR2(20),
	Midterm	NUMBER(3,0) 	CHECK (Midterm>=0 AND Midterm<=100),
	Final		NUMBER(3,0)	CHECK (Final>=0 AND Final<=100),
	Homework	NUMBER(3,0)	CHECK (Homework>=0 AND Homework<=100),
	PRIMARY KEY (ID)
);
INSERT INTO STUDENT VALUES ( '445', 'Seinfeld', 86, 90, 99 );
INSERT INTO STUDENT VALUES ( '909', 'Costanza', 74, 72, 86 );
INSERT INTO STUDENT VALUES ( '123', 'Benes', 93, 89, 91 );
INSERT INTO STUDENT VALUES ( '111', 'Kramer', 99, 91, 93 );
INSERT INTO STUDENT VALUES ( '667', 'Newman', 77, 82, 84 );
INSERT INTO STUDENT VALUES ( '889', 'Banya', 52, 66, 50 );
SELECT * FROM STUDENT;

DROP TABLE WEIGHTS CASCADE CONSTRAINTS;
CREATE TABLE WEIGHTS(
	MidPct	NUMBER(2,0) CHECK (MidPct>=0 AND MidPct<=100),
	FinPct	NUMBER(2,0) CHECK (FinPct>=0 AND FinPct<=100),
	HWPct	NUMBER(2,0) CHECK (HWPct>=0 AND HWPct<=100)
);
INSERT INTO WEIGHTS VALUES ( 30, 30, 40 );
SELECT * FROM WEIGHTS;
COMMIT;



SET SERVEROUTPUT ON;


DECLARE
    midweight number;
    finweight number;
    hweight number;
    avggrade number;
    lettergrade varchar(3);
    
    
    cursor st_cursor IS
        (SELECT ID, Name, Midterm, Final, Homework FROM student);
    stuid student.id%type;
    stuname student.name%type;
    stumid student.midterm%type;
    stufin student.final%type;
    stuhom student.homework%type;
  
 
BEGIN
    SELECT MIDPCT INTO midweight FROM WEIGHTS;
    SELECT FINPCT INTO finweight FROM WEIGHTS;
    SELECT HWPCT INTO hweight FROM WEIGHTS;
    dbms_output.put_line('Weights are ' || midweight || ' '  || finweight || ' ' || hweight);

    
    open st_cursor;
    loop
        fetch st_cursor INTO stuid, stuname, stumid, stufin, stuhom;
        avggrade := round((stumid + stufin + stuhom) / 3, 2);
        exit when st_cursor%notfound;
        
 IF avggrade > 90 THEN
    lettergrade := 'A';
  ELSIF avggrade > 80 THEN
    lettergrade := 'B';
  ELSIF avggrade > 70  THEN
    lettergrade := 'C';
  ELSIF avggrade > 60 THEN
    lettergrade := 'D';
  ELSIF avggrade > 0 THEN
    lettergrade := 'F';
  ELSE
    lettergrade := 'NULL';
  END IF;
        
        dbms_output.put_line(stuid || ' ' || stuname || ' ' || avggrade || ' ' || lettergrade);
    end loop;
    close st_cursor;
 
END;

/