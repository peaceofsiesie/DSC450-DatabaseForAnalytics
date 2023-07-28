-- Drop Table
DROP TABLE creditcard;

-- Create Table


CREATE TABLE creditcard
(

c_id Number(5), 
c_name VARCHAR2(30),
c_number VARCHAR2(19),
c_date VARCHAR(5),
c_csv NUMBER(3),

            PRIMARY KEY (c_id),

            CONSTRAINT c_number_format
                        CHECK
                        ( REGEXP_LIKE (c_number, '\d{4}-?\d{4}-?\d{4}-?\d{4}')),
                        
            CONSTRAINT c_date_format
                        CHECK
                        ( REGEXP_LIKE (c_date, '\d?\d/\d{2}'))
            

);


insert into creditcard
    values (1, 'Sierra Salaam', '5424-3216-4590-8539', '10/30', 200);
insert into creditcard
    values (2, 'Summer Walker', '59263217893408576', '9/30', 387);
insert into creditcard
    values (3, 'Kandy Smith', '0426-3298-7937-0832', '02/30', 530);
    
SELECT * FROM creditcard;