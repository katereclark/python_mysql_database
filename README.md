# Overview

I created this software to increase my understanding of how to integrate SQL commands into Python code and how to connect to a SQL server. This program connects to the MySQL local server and adds an employees_info database and an employees table and a departments table if they are not already present. It allows a user to display, add, edit, and remove employees and to display and add departments. The user can select an option from the menu in the terminal and follow the prompts to completion. My purpose for building this software is to create and maintain a relational database that imitates database of employees and departments and stores each individual's information.

Here is a demo of my software: [Software Demo Video](https://youtu.be/Pipy8jTu9k4)

# Relational Database

I created this relational database using MySQL commands in Python code using the mysql.connector module. The database is called employees_info and contains two tables: employees and departments. The employees table contains the fields: id (primary key), first_name, last_name, date_hired, hourly_wage, and departments_id (foreign key). The departments table contains the fields: id (primary key) and dept_name. The tables can be joined using the employees.departments_id and departments.id.

# Development Environment

* Visual Studio Code
* Python 3.8.5 32-bit
* Git / GitHub
* mysql.connector module - allows a user to connect to their local MySQL server

# Useful Websites

* [MySQL Python Connector Guide](https://dev.mysql.com/doc/connector-python/en/)
* [Basic SQL Commands](https://www.w3schools.com/sql/)
* [Using Python with MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)

# Future Work

* Add the capability to remove and modify departments as well.
* Have each department contain all of the employees rather than repeating the department for every employee in the inner join.
* Put in more fields in the employees and departments tables, like gender, availability, department abbreviations, etc.
