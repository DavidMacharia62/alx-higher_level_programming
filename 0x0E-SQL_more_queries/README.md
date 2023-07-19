# SQL

## MORE SQL QUERIES

## How to create a new MySQL user:

To create a new MySQL user, you'll need appropriate privileges, typically granted to administrative users like 'root'. Use the CREATE USER statement to create a new user:

* sql code
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';

This example creates a user named 'new_user' with the password 'password'. The '@' symbol followed by 'localhost' indicates that this user can only connect from the local machine.

## How to manage privileges for a user to a database or table:

To grant privileges to a user on a specific database or table, you can use the GRANT statement. For example, to grant all privileges on a database called 'your_database' to 'new_user':

* sql code
GRANT ALL PRIVILEGES ON your_database.* TO 'new_user'@'localhost';

## To grant specific privileges (e.g., SELECT, INSERT, UPDATE, DELETE) on a particular table:

* sql code
GRANT SELECT, INSERT ON your_database.your_table TO 'new_user'@'localhost';

After granting privileges, you should run the FLUSH PRIVILEGES; command to apply the changes.

## What's a PRIMARY KEY:

A PRIMARY KEY is a column or a combination of columns that uniquely identifies each record in a database table. It ensures data integrity and enforces the uniqueness constraint on the specified column(s). In MySQL, you can define a PRIMARY KEY when creating a table:

* sql code
CREATE TABLE your_table (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
Here, the 'id' column is designated as the primary key.

## What's a FOREIGN KEY:

A FOREIGN KEY is a column or a combination of columns in a table that refers to the PRIMARY KEY of another table. It establishes a link between the data in two tables and maintains referential integrity. In MySQL, you can define a FOREIGN KEY constraint when creating a table:

* sql code
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  product_id INT,
  customer_id INT,
  FOREIGN KEY (product_id) REFERENCES products (product_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

Here, the 'product_id' and 'customer_id' columns are FOREIGN KEYs that reference the 'product_id' and 'customer_id' columns in the 'products' and 'customers' tables, respectively.

## How to use NOT NULL and UNIQUE constraints:

The NOT NULL constraint ensures that a column must contain a non-null value, while the UNIQUE constraint enforces that the values in the column must be unique across all records in the table.

Example using NOT NULL:

* sql code
CREATE TABLE your_table (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  age INT
);
In this example, both 'name' and 'email' columns must have non-null values, and the 'email' column must contain unique values.

## How to retrieve data from multiple tables in one request:
You can use SQL JOIN clauses to retrieve data from multiple tables in a single query. For example, suppose you have two tables, 'orders' and 'customers', and you want to get a list of orders with the corresponding customer names:

* sql code
SELECT orders.order_id, orders.order_date, customers.customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;
The JOIN keyword combines the 'orders' table with the 'customers' table based on the 'customer_id' column.

## What are subqueries:

A subquery, also known as an inner query or nested query, is a query within another query. It allows you to use the results of one query as a condition or data source for another query. Subqueries are enclosed within parentheses and can appear in various parts of an SQL statement, such as the WHERE clause or FROM clause.

Example of a subquery in the WHERE clause:

* sql code
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);
In this example, the subquery (SELECT AVG(price) FROM products) calculates the average price of all products, and the outer query retrieves products with prices higher than the average.

## What are JOIN and UNION:

JOIN: As mentioned earlier, JOIN is used to combine rows from two or more tables based on related columns between them. It allows you to retrieve data from multiple tables simultaneously, creating a single result set. We saw an example of an inner join above.

There are different types of joins: INNER JOIN, LEFT JOIN (or LEFT OUTER JOIN), RIGHT JOIN (or RIGHT OUTER JOIN), and FULL JOIN (or FULL OUTER JOIN). Each type determines how the data is combined and what happens when there is no match between the joined tables.

UNION: UNION is used to combine the results of two or more SELECT queries into a single result set. The SELECT queries must have the same number of columns, and the data types of the corresponding columns must be compatible.

Example of UNION:

* sql code
SELECT product_name FROM table1
UNION
SELECT product_name FROM table2;
In this example, the results of the two SELECT queries are combined, removing any duplicate entries, and the final result contains a list of distinct product names from both 'table1' and 'table2'.
