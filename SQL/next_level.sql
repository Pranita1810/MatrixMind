USE testing;

---- JOINS ----
-- INNER JOIN: Returns records that have matching values in both tables
SELECT E.emp_id, E.name, D.dept_name
FROM Employees E
INNER JOIN Departments D ON E.dept_id = D.dept_id;

-- LEFT (OUTER) JOIN: Returns all records from left table, and matched records from right table
SELECT E.emp_id, E.name, D.dept_name
FROM Employees E
LEFT JOIN Departments D ON E.dept_id = D.dept_id;

-- RIGHT (OUTER) JOIN: Returns all records from right table, and matched records from left table
SELECT E.emp_id, E.name, D.dept_name
FROM Employees E
RIGHT JOIN Departments D ON E.dept_id = D.dept_id;

-- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
SELECT E.emp_id, E.name, D.dept_name
FROM Employees E
FULL OUTER JOIN Departments D ON E.dept_id = D.dept_id;


---- AGGREGATES & GROUP BY ----
-- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
SELECT dept_id,
       COUNT(*) AS employee_count,
       SUM(salary) AS total_salary,
       AVG(salary) AS average_salary,
       MIN(salary) AS min_salary,
       MAX(salary) AS max_salary
FROM Employees
GROUP BY dept_id;

-- HAVING: Filters groups after aggregation
SELECT dept_id, SUM(salary) AS total_salary
FROM Employees
GROUP BY dept_id
HAVING SUM(salary) > 70000;


---- WINDOW FUNCTIONS ----
-- ROW_NUMBER, RANK, and DENSE_RANK
SELECT emp_id,
       name,
       dept_id,
       salary,
       ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num,
       RANK()       OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_pos,
       DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank_pos
FROM Employees;
