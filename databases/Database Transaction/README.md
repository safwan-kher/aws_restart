# Database Interaction and Transaction

Here you are provided a step-by-step guide to understanding database interactions and transactions. We will cover different roles that interact with databases, transaction states in a Database Management System (DBMS), and primary models for database interaction.

## Exercise 1: Understanding Roles that Interact with Databases

1. **End Users**: These are the individuals who interact with databases through an application. They use the system to retrieve and manipulate data for their specific needs.

2. **Data Analysts**: They interact with the database to analyze data and derive insights. They use various data analysis tools and techniques to extract, process, and interpret data.

3. **Database Administrators**: They are responsible for managing and maintaining the database. Their tasks include ensuring data integrity, implementing security measures, and optimizing database performance.

4. **Application Developers**: They build applications that interact with the database. They write code to create, retrieve, update, and delete data in the database.

## Exercise 2: Understanding Transaction States in a DBMS

1. **Active State**: This is the initial state of every transaction when it is being executed.

2. **Partially Committed State**: A transaction is in this state when it is in the process of completing its final operation.

3. **Failed State**: A transaction enters this state when any checks made by the database recovery system fail.

4. **Aborted State**: If a transaction fails any checks and enters a failed state, it is then aborted. The database reverts to its original state prior to the transaction's execution.

5. **Committed State**: Once all operations within a transaction have been successfully executed, the transaction is considered committed. This means the changes made by the transaction are now permanent in the database.

## Exercise 3: Understanding Primary Models for Database Interaction

1. **Client-Server Model**: In this model, the client sends requests to the server which then interacts with the database. The server processes the request, interacts with the database, and sends the response back to the client.

2. **Application Developer Interaction**: Here, developers build applications that interact directly with the database. They write code to perform CRUD (Create, Read, Update, Delete) operations on the database.

3. **Three-Tier Application with Web Application**: This model includes a user interface, functional process logic (business logic), and a database. The user interface sends requests to the business logic layer, which then interacts with the database.

By understanding these concepts, you will have a solid foundation in database interactions and transactions.