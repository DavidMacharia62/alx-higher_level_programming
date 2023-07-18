# SQL

## What's a database?

A database is a structured collection of data organized and stored in a way that allows efficient retrieval, updating, and management of information. It provides a systematic approach to managing data, making it easier to store, access, and modify information as needed.

## What's a relational database?

A relational database is a type of database that stores and organizes data in tables with predefined relationships between them. It uses a relational model based on mathematical set theory, where data in different tables can be related through common fields, known as keys.

## What does SQL stand for?

SQL stands for "Structured Query Language." It is a standardized programming language used to communicate with and manage relational databases. SQL allows users to define, manipulate, and control data within the database.

## What's MySQL?

MySQL is an open-source relational database management system (RDBMS) based on SQL. It is widely used for web-based applications and is known for its performance, ease of use, and scalability. MySQL supports multiple platforms and is commonly used in conjunction with PHP to power dynamic web applications.

## How to create a database in MySQL?

To create a database in MySQL, you can use the SQL command "CREATE DATABASE." For example:

CREATE DATABASE your_database_name;
What does DDL and DML stand for?
DDL stands for "Data Definition Language," and it includes SQL commands used to define and manage the structure of a database, such as creating, altering, or dropping tables, indexes, and other database objects.
DML stands for "Data Manipulation Language," and it includes SQL commands used to retrieve, insert, update, and delete data within the database.

## How to CREATE or ALTER a table?

To create a new table in MySQL, you use the "CREATE TABLE" statement. Here's an example:

* CREATE TABLE your_table_name (
    column1 datatype1 constraint1,
    column2 datatype2 constraint2,
    ...
);

To alter an existing table, you use the "ALTER TABLE" statement to add, modify, or remove columns. For example, to add a new column:

* ALTER TABLE your_table_name
ADD column_name datatype;
How to SELECT data from a table?

## To retrieve data from a table in MySQL, you use the "SELECT" statement. Here's a basic example to fetch all columns from a table:

* SELECT * FROM your_table_name;
You can also specify particular columns and use conditions to filter data using the "WHERE" clause:

* SELECT column1, column2 FROM your_table_name WHERE condition;

## How to INSERT, UPDATE, or DELETE data?
To insert new data into a table, you use the "INSERT INTO" statement:

* INSERT INTO your_table_name (column1, column2, ...)
VALUES (value1, value2, ...);

## To update existing data in a table, you use the "UPDATE" statement:

* UPDATE your_table_name
SET column1 = new_value1, column2 = new_value2
WHERE condition;
## To delete data from a table, you use the "DELETE FROM" statement:

* DELETE FROM your_table_name
WHERE condition;

## What are subqueries?

A subquery, also known as an inner query or nested query, is a query within another query. It allows you to retrieve data from one or more tables based on the results of another query. Subqueries are enclosed within parentheses and can be used in SELECT, INSERT, UPDATE, or DELETE statements.

## How to use MySQL functions?

MySQL provides a variety of built-in functions that perform various tasks, such as manipulating data, performing calculations, or formatting output. Here's a basic example of using the COUNT function to count the number of rows in a table:

* SELECT COUNT(*) FROM your_table_name;
MySQL offers many other functions like SUM, AVG, MAX, MIN, CONCAT, DATE_FORMAT, etc. You can use these functions in combination with your SQL queries to achieve the desired results based on your specific requirements.
