-- 1. CREATE A DDL_Learn DataBase --
CREATE DATABASE DDL_Learn


--************************************************************************************************************************************************************************************


-- 2. Create a new table called employees --
-- SSMS --
CREATE TABLE Employee_Info (
    ID BIGINT PRIMARY KEY IDENTITY(1,1),
    Emp_Name VARCHAR(50) NOT NULL,
    Department VARCHAR(50),
    Salary DECIMAL(10,3) NOT NULL CHECK (Salary > 0),
    )

-- PG --
CREATE TABLE Employee_Info(
    employee_id BIGINT GENERATED ALWAYS AS IDENTITY,
    Emp_Name VARCHAR(50) NOT NULL,
    Department VARCHAR(50),
    Salary DECIMAL(10,3) NOT NULL CHECK (Salary > 0)
    )


--************************************************************************************************************************************************************************************


-- 3. Alter table, add email column, change salary type to (12,2), rename emp_name to employee_name. --
-- SSMS --
ALTER TABLE Employee_Info ADD Email VARCHAR(30)
ALTER TABLE Employee_Info ALTER COLUMN Salary DECIMAL(12,2) 
EXEC sp_rename "Employee_Info.Employee_Namee", "Employee_Name" , "COLUMN"
-- PG --
ALTER TABLE Employee_Info ADD COLUMN Email VARCHAR(30)
ALTER TABLE Employee_Info ALTER COLUMN Salary TYPE DECIMAL(12,2)
ALTER TABLE Employee_Info RENAME COLUMN Emp_Name TO Employee_Name 


--************************************************************************************************************************************************************************************


-- 4. Remove ID 3, Reset Identity, Remove all values, Delete entire table --
-- SSMS --
DELETE FROM Employee_Info WHERE ID = 3
TRUNCATE TABLE Employee_Info
DROP TABLE Employee_Info;

-- PG --
DELETE FROM Employee_INFO WHERE employee_id = 3
TRUNCATE TABLE Employee_Info RESTART IDENTITY
DROP TABLE Employee_Info 



