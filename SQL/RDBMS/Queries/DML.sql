---- DML ----

-- 1. Insert new records in existing table.
-- SSMS --
INSERT INTO Customers( customer_name,email,phone_number,customer_status)
VALUES ('Pranit Ugale', 'pranitugale1000@gmail.com', 8850559967 , 'Active')
INSERT INTO Customers(customer_name,email, phone_number)
VALUES('Hemant', 'jhemant90@gmail.com', 8855669954)
-- PG --
INSERT INTO Customers(customer_name, email, customer_status, phone_number)
VALUES ('Pranit Ugale', 'pranitugale1000@gmail.com', 'Active', 8850559967 )
INSERT INTO Customers(customer_name,email, phone_number)
VALUES('Hemant', 'jhemant90@gmail.com', 8855669954)


-- ######################################################################################################################################################
-- 2. UPDATE (Change customer's name) --
-- SSMS & PG --
UPDATE Customers SET customer_name = 'Ye Leng' WHERE customer_id = 2


-- ######################################################################################################################################################
-- 3. UPDATE Multiple columns & multiple rows
UPDATE Customers SET
customer_name = 'xi jumping',
email = 'xijumping69@gmail.com',
phone_number = 6969696969
WHERE customer_id = 5

-- ######################################################################################################################################################
-- 4. DELETE
DELETE FROM Customers WHERE customer_id = 20
SELECT * FROM Customers ORDER BY customer_id ASC;   
SELECT * FROM Orders


