---------------- **DATA MODIFICATION LANGUAGE** ----------------



--- 1. INSERT 5 customers into Customers using a single insert statement ---
-- SSMS & PG--
INSERT INTO Customers(customer_name, email, customer_status, phone_number)
VALUES ('Ritik bacha', 'ritkichikna10@gmail.com','Inactive',9632147551),
        ('Rohan Kulkarni', 'rohan.kulkarni30@gmail.com', 'Active', 9823456710),
        ('Priya Deshmukh', 'priya.deshmukh40@gmail.com', 'Active', 9765432180),
        ('Kunal Jadhav', 'kunal.jadhav50@gmail.com', 'Inactive', 9654321870),
        ('Neha Pawar', 'neha.pawar60@gmail.com', 'Active', 9543218760),
        ('Aditya More', 'aditya.more70@gmail.com', 'Inactive', 9432167850),
        ('Isha Joshi', 'isha.joshi80@gmail.com', 'Active', 9321678540),
        ('Siddharth Shah', 'siddharth.shah90@gmail.com', 'Active', 9216785430)



-- 2. INSET 5 orders into Orders for existing customers
-- SSMS & PG --
INSERT INTO Orders (item_name,price,quantity, customer_id)
VALUES ('Dish washer', 2.2, 14, 1),
    ('Dish washer', 2.2, 14, 1),
    ('Washing Machine', 3.5, 8, 2),
    ('Refrigerator', 4.8, 17, 5),
    ('Microwave Oven', 1.9, 5, 6),
    ('Air Conditioner', 5.2, 12, 7),
    ('Vacuum Cleaner', 2.7, 19, 8),
    ('Water Purifier', 3.1, 6, 9),
    ('Ceiling Fan', 4.4, 11, 10),
    ('Electric Kettle', 1.5, 3, 11),
    ('Toaster', 2.9, 16, 12),
    ('Coffee Maker', 3.8, 9, 13),
    ('Induction Cooktop', 4.2, 20, 14),
    ('Rice Cooker', 2.4, 7, 15),
    ('Mixer Grinder', 5.5, 13, 16),
    ('Water Heater', 3.6, 4, 17),
    ('Electric Iron', 1.8, 15, 18),
    ('Room Heater', 4.7, 10, 19),
    ('Air Cooler', 2.6, 18, 21),
    ('LED Television', 5.9, 2, 22),
    ('Bluetooth Speaker', 3.3, 14, 23);




-- 3. UPDATE a cusomer's email where id is 6
-- SSMS & PG --
UPDATE Customers SET email = 'ngiachiga6969@gmail.com'
WHERE customer_id = 6


-- 4. UPDATE the phone number & email of a customer in a single statement
UPDATE Customers SET email = 'greatescape22@gmail.com', phone_number = 452784125
WHERE customer_id = 7


-- 5. Increase the price of all orders by 10%
UPDATE Orders SET price = price+price*10/100


-- 6. Increase the quantity of all oerders by 2 where the item name is 'Dish washer'
UPDATE Orders SET quantity = quantity+2 WHERE item_name = 'Dish washer'


-- 7. Delete orders where quantity is 0 
DELETE FROM Orders WHERE quantity = 0


-- 8. Increase price for inactive customers using subquery
UPDATE Orders SET price = price*2
WHERE customer_id IN (SELECT customer_id FROM Customers WHERE customer_status = 'Inactive')


-- 9. Delete orders belonging to customers whose email ends with yahoo.com, using a subquery.
DELETE FROM Orders WHERE customer_id IN
(SELECT customer_id FROM Customers WHERE email LIKE '%.com')


-- 10. Delete customers who never placed any order
DELETE FROM Customers WHERE customer_id NOT IN
(SELECT customer_id FROM Orders)


-- 11. If any customer is deleted it should delete it's order too
DELETE FROM Customers WHERE customer_id = 23 
SELECT * FROM Customers
SELECT * FROM Orders


-- 12. Delete a customer using DELETE and verify the effect of ON DELETE CASCADE.
ALTER TABLE Orders DROP CONSTRAINT fk_customer_id_set_null_if_deleted
ALTER TABLE Orders ADD CONSTRAINT fk_customer_id_delete_cascade FOREIGN KEY(customer_id)
REFERENCES Customers(customer_id) ON DELETE CASCADE
DELETE FROM Customers WHERE customer_id = 1

SELECT * FROM Orders
SELECT * FROM Customers
