# SQL Exercises
These exercises will cover string, date and time, numeric data types, constraints, and foreign keys. 
The exercises will be based on an e-commerce database with two tables: 'Customers' and 'Orders'.
## Setup

Create the 'Customers' and 'Orders' tables:

```sql
CREATE TABLE Customers (
    CustomerID int NOT NULL,
    FirstName varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    BirthDate date,
    PRIMARY KEY (CustomerID)
);

CREATE TABLE Orders (
    OrderID int NOT NULL,
    CustomerID int,
    OrderDate date NOT NULL,
    OrderAmount decimal(10,2) NOT NULL,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

## Exercises

1. Insert a new customer into the 'Customers' table:

```sql
INSERT INTO Customers (CustomerID, FirstName, LastName, BirthDate)
VALUES (1, 'John', 'Doe', '1980-01-01');
```

2. Insert a new order for the customer you just inserted:

```sql
INSERT INTO Orders (OrderID, CustomerID, OrderDate, OrderAmount)
VALUES (1, 1, '2022-01-01', 100.00);
```

3. Update the last name of the customer you inserted:

```sql
UPDATE Customers
SET LastName = 'Smith'
WHERE CustomerID = 1;
```

4. Increase the order amount of the order you inserted by 10%:

```sql
UPDATE Orders
SET OrderAmount = OrderAmount * 1.1
WHERE OrderID = 1;
```

5. Select all customers who were born before 1990:

```sql
SELECT *
FROM Customers
WHERE BirthDate < '1990-01-01';
```

6. Select all orders that were placed in 2022:

```sql
SELECT *
FROM Orders
WHERE OrderDate >= '2022-01-01' AND OrderDate < '2023-01-01';
```

7. Delete the order you inserted:

```sql
DELETE FROM Orders
WHERE OrderID = 1;
```

8. Try to delete the customer you inserted (it should fail because there's a foreign key constraint):

```sql
DELETE FROM Customers
WHERE CustomerID = 1;
```

9. Delete the foreign key constraint from the 'Orders' table, then try to delete the customer again:

```sql
ALTER TABLE Orders
DROP FOREIGN KEY FK_Orders_Customers;

DELETE FROM Customers
WHERE CustomerID = 1;
```

10. Drop the 'Customers' and 'Orders' tables:

```sql
DROP TABLE Orders;
DROP TABLE Customers;
```
```

Remember to replace the foreign key constraint name (`FK_Orders_Customers`) with the actual name in your database.