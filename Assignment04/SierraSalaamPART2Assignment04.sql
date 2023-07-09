DROP TABLE Employer;
DROP TABLE JobDetails;


CREATE TABLE JobDetails
(
  JName       VARCHAR2(50),
  JSalary     VARCHAR(30),
  JAssistant  VARCHAR(3),
  
    CONSTRAINT JobDetails_PK
        PRIMARY KEY(JName)
);


CREATE TABLE Employer
(
  EFirst    VARCHAR2(25),
  ELast     VARCHAR2(25),
  EAddress  VARCHAR2(150),
  EJob      VARCHAR2(50) NOT NULL,

  
  CONSTRAINT Employer_PK1
     PRIMARY KEY(EFirst, ELast, EJob),

    CONSTRAINT Employer_FK1
        FOREIGN KEY(EJob)
            REFERENCES JobDetails(JName)
);



