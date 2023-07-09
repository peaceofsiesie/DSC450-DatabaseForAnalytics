/* Drop Tables already exisiting */
Drop TABLE STUDENT;
Drop TABLE ADVISORS;
Drop Table DEPARTMENT;

/*Create Tables */

/*Create Department Table*/
CREATE TABLE Department (

    Name VARCHAR2(50),
    Chair NUMBER(5),
    CollegeName NUMBER(5),
    
    CONSTRAINT Department_PK
        PRIMARY KEY(Name)
        
);

/*Create Advisors Table*/
CREATE TABLE Advisors (

    ID NUMBER(5),
    Name VARCHAR2(50) NOT NULL,
    Address VARCHAR2(50),
    ResearchArea VARCHAR2(50),
    DepartmentName VARCHAR2(50), 
    
    CONSTRAINT Advisors_PK
        PRIMARY KEY (ID),
        
    CONSTRAINT Advisors_FK1
        FOREIGN KEY (DepartmentName)
            REFERENCES Department(Name)

);

/*Create STUDENT Table*/
CREATE TABLE STUDENT (

    ID NUMBER(5),
    LastName VARCHAR2(50) NOT NULL,
    FirstName VARCHAR2(50),
    Birthdate DATE,
    Telephone VARCHAR(13),
    AdvisorsID NUMBER(5), 
    
    CONSTRAINT Student_PK
        PRIMARY KEY (ID),
        
    CONSTRAINT Student_FK1
        FOREIGN KEY (AdvisorsID)
            REFERENCES Advisors(ID)
        
);



