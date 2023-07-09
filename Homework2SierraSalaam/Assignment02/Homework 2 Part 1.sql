/* Drop Tables already exisiting */
Drop Table BooksWritten;
Drop TABLE Books;
Drop TABLE Publisher;
Drop TABLE Authors;

/*Create Tables */

/*Create Authors Table*/
CREATE TABLE Authors (

    ID NUMBER(5),
    LastName VARCHAR2(50) NOT NULL,
    FirstName VARCHAR2(50),
    Birthdate DATE,
    
    CONSTRAINT Authors_PK
        PRIMARY KEY (ID)

);

/*Create Publisher Table*/
CREATE TABLE Publisher (

    ID NUMBER(5), 
    Name VARCHAR2(100) NOT NULL,
    Address VARCHAR2(255),
    
    CONSTRAINT Publisher_PK
        PRIMARY KEY (ID)

);

/*Create Books Table*/
CREATE TABLE Books (

    ISBN VARCHAR2(10),
    Title VARCHAR2(100),
    PublisherID NUMBER(5),
    
    CONSTRAINT Books_PK
        PRIMARY KEY (ISBN),
        
    CONSTRAINT Books_FK1
        FOREIGN KEY (PublisherID)
            REFERENCES Publisher(ID)

);

/*Create BooksWritten Table*/
CREATE TABLE BooksWritten (

    BookID VARCHAR2(10),
    AuthorsID NUMBER(5),
    Placement NUMBER(5),
    
    CONSTRAINT BW_PK
        PRIMARY KEY(BookID, AuthorsID),
        
    CONSTRAINT BW_FK1
        FOREIGN KEY (BookID)
            REFERENCES Books(ISBN),
    
     CONSTRAINT BW_FK2
        FOREIGN KEY (AuthorsID)
            REFERENCES Authors(ID)

);

/*Add New Data To Tables*/

/*Add Data To Authors Table*/
INSERT INTO authors(lastname, firstname, id, birthdate) 
    VALUES ('King', 'Stephen', 2, to_date('September 9, 1947', 'Month dd, YYYY'));
    
INSERT INTO authors(lastname, firstname, id, birthdate) 
    VALUES ('Asimov', 'Isaac', 4, to_date('January 2 1921', 'Month dd, YYYY'));

INSERT INTO authors(lastname, firstname, id, birthdate) 
    VALUES ('Verne', 'Jules', 7, to_date('February 8 1828', 'Month dd, YYYY'));

INSERT INTO authors(lastname, firstname, id, birthdate) 
    VALUES ('Shelley', 'Mary', 37, to_date('August 30 1797', 'Month dd, YYYY'));

/* Add Data To Publisher Table*/
INSERT INTO publisher(name, id, address) 
    VALUES ('Bloomsbury Publishing', 17, 'London Borough of Camden');
    
INSERT INTO publisher(name, id, address)
    VALUES ('Arthur A Levine Books', 18, 'New York City');

/* Add Data To Books Table*/
INSERT INTO books(isbn, title, publisherid) 
    VALUES ('1111-111', 'Databases from Outer Space', 17);
    
INSERT INTO books(isbn, title, publisherid) 
    VALUES ('2223-233', 'Revenge of SQL', 17);

INSERT INTO books(isbn, title, publisherid) 
    VALUES ('3333-332', 'The Night of the Living Databases', 18);


/* Add Data To BOOKSWRITTEN Table*/    
INSERT INTO bookswritten(authorsid, bookid, placement) 
    VALUES (2, '1111-111', 1);
    
INSERT INTO bookswritten(authorsid, bookid, placement)
    VALUES (4, '1111-111', 2);

INSERT INTO bookswritten(authorsid, bookid, placement)
    VALUES (4, '2223-233', 1);

INSERT INTO bookswritten(authorsid, bookid, placement)
    VALUES (7, '2223-233', 2);

INSERT INTO bookswritten(authorsid, bookid, placement)
    VALUES (37, '3333-332', 1);

INSERT INTO bookswritten(authorsid, bookid, placement)
    VALUES (2, '3333-332', 2);
    

