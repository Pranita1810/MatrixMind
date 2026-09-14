-- DDL --
-- Creating db & table --
CREATE DATABASE testing 
USE testing

CREATE TABLE pranit_info(
sr_id INT,
Name Varchar(50),
salary INT)

-- Alter table : Add/Delete/Modify column in table
ALTER TABLE pranit_info
ADD Age INT
ALTER TABLE pranit_info
ALTER COLUMN salary FLOAT
ALTER TABLE pranit_info
DROP column Age


-- DML 
-- INSERT DATA
INSERT INTO pranit_info (sr_id, Name, salary)
VALUES (1, 'pranit' ,21000),
		(2, 'harsh', 18000),
		(3, 'hemant', 40000),
				(4, 'hemant', 40000)
-- UPDATE DATA
UPDATE pranit_info SET salary = 50000 WHERE sr_id=1
-- DELETE DATA : Delete rows from table
DELETE FROM pranit_info where sr_id = 1

 

SELECT * FROM pranit_info;

-- Find second highest salary using subquery
SELECT MAX(salary) AS second_highest_salary 
FROM pranit_info 
WHERE salary < (SELECT MAX(salary) FROM pranit_info);

-- Find duplicate count
SELECT Name, COUNT(*) AS duplicate_count 
FROM pranit_info 
GROUP BY Name 
HAVING COUNT(*) > 1;

-- Delete duplicate records using CTE and ROW_NUMBER()
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY Name ORDER BY sr_id) AS rn 
    FROM pranit_info
)
DELETE FROM CTE WHERE rn > 1;


