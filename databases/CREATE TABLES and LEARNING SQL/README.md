# SQL Exercises
These exercises will cover string, date and time, numeric data types, constraints, and foreign keys. 
The exercises will be based on an e-commerce database with two tables: 'Customers' and 'Orders'.
## Setup

Create the 'Customers' and 'Orders' tables:



## Exercises

1. Insert a new customer into the 'Customers' table:



2. Insert a new order for the customer you just inserted:



3. Update the last name of the customer you inserted:



4. Increase the order amount of the order you inserted by 10%:



5. Select all customers who were born before 1990:



6. Select all orders that were placed in 2022:



7. Delete the order you inserted:


8. Try to delete the customer you inserted (it should fail because there's a foreign key constraint):



9. Delete the foreign key constraint from the 'Orders' table, then try to delete the customer again:



10. Drop the 'Customers' and 'Orders' tables:



Remember to replace the foreign key constraint name (`FK_Orders_Customers`) with the actual name in your database.