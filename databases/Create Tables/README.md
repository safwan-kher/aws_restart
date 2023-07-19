Sure, here are 10 exercises for beginners to practice creating tables, inserting data, and querying data in SQL. 

```markdown
# SQL Exercises

## Exercise 1: Creating a Table
Create a table named 'Books' with the following columns: 'ID', 'Title', 'Author', 'PublicationYear', and 'Price'.

Hint:
```sql
CREATE TABLE Books (
    ID int,
    Title varchar(255),
    Author varchar(255),
    PublicationYear int,
    Price decimal(5,2)
);
```

## Exercise 2: Inserting Data
Insert the following data into the 'Books' table:

1. ID: 1, Title: 'Book1', Author: 'Author1', PublicationYear: 2000, Price: 10.99
2. ID: 2, Title: 'Book2', Author: 'Author2', PublicationYear: 2005, Price: 15.99
3. ID: 3, Title: 'Book3', Author: 'Author3', PublicationYear: 2010, Price: 20.99

Hint:
```sql
INSERT INTO Books (ID, Title, Author, PublicationYear, Price) 
VALUES (1, 'Book1', 'Author1', 2000, 10.99);
```

## Exercise 3: Querying Data
Write a SQL query to fetch all records from the 'Books' table.

Hint:
```sql
SELECT * FROM Books;
```

## Exercise 4: Updating Data
Update the price of the book with ID 1 to 12.99.

Hint:
```sql
UPDATE Books SET Price = 12.99 WHERE ID = 1;
```

## Exercise 5: Deleting Data
Delete the record of the book with ID 2 from the 'Books' table.

Hint:
```sql
DELETE FROM Books WHERE ID = 2;
```

## Exercise 6: Creating a Table with Primary Key
Create a table named 'Students' with the following columns: 'ID' (primary key), 'Name', and 'Age'.

Hint:
```sql
CREATE TABLE Students (
    ID int PRIMARY KEY,
    Name varchar(255),
    Age int
);
```

## Exercise 7: Inserting Data with Primary Key
Insert the following data into the 'Students' table:

1. ID: 1, Name: 'Student1', Age: 20
2. ID: 2, Name: 'Student2', Age: 22

Hint:
```sql
INSERT INTO Students (ID, Name, Age) 
VALUES (1, 'Student1', 20);
```

## Exercise 8: Querying Data with Condition
Write a SQL query to fetch all records from the 'Students' table where 'Age' is greater than 21.

Hint:
```sql
SELECT * FROM Students WHERE Age > 21;
```

## Exercise 9: Updating Data with Condition
Update the age of the student with ID 1 to 21.

Hint:
```sql
UPDATE Students SET Age = 21 WHERE ID = 1;
```

## Exercise 10: Deleting Data with Condition
Delete the record of the student with ID 2 from the 'Students' table.

Hint:
```sql
DELETE FROM Students WHERE ID = 2;
```
```
These exercises cover the basic operations in SQL: creating tables, inserting data, querying data, updating data, and deleting data. They also introduce the concept of primary keys.