CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DOUBLE
);
INSERT INTO employee VALUES
(101, 'Rahul', 'IT', 50000),
(102, 'Anjali', 'HR', 45000),
(103, 'Arjun', 'Finance', 60000);
