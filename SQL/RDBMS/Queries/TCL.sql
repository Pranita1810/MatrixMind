-- TCL is a subset of sql which manages how transactions are executed and rolled back in databases. Basically user can execute a group of queries if one fails previous will be rolled back.


----- TCL TASKS -----
-- 1. Start a transaction, chnages Neha's status from active to inactive, verify, rollback verify
-- SSMS --
BEGIN TRANSACTION
UPDATE Customers SET customer_status = 'Inactive' WHERE customer_name = 'Neha Pawar';
ROLLBACK;

-- PG4 --
BEGIN
UPDATE Customers SET customer_status = 'Inactive' WHERE customer_name = 'Ira Pawar'
ROLLBACK



-- 2. Execute : Update email, delete entry, insert new entry. SavePoint on every execution only rollback previous if the current is failed.IMMUTABLE
-- SSMS --
BEGIN TRANSACTION
UPDATE Customers SET email = 'nigulig200@gmail.com' WHERE customer_id = 11
SAVE TRANSACTION sp1;
DELETE FROM Customers WHERE customer_id = 8
SAVE TRANSACTION sp2
INSERT INTO Customers(customer_name, email, customer_status, phone_number)
VALUES ('Pranit Chan', 'pranitchan000@gmail.cPom', 'Active', 9821221145)
SAVE TRANSACTION sp3
ROLLBACK TRANSACTION sp2
COMMIT




BEGIN;

UPDATE Customers
SET customer_status = 'Inactive'
WHERE customer_name = 'Neha Pawar';

-- Inner transaction
BEGIN;

UPDATE Customers
SET customer_status = 'Active'
WHERE customer_name = 'Neha Pawar';

ROLLBACK;

COMMIT;


SELECT * FROM Customers WHERE customer_name = 'Ira Pawar';
SELECT * FROM Orders;