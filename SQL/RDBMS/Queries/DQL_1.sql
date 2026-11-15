-- Topics : SELECT, WHERE, AND, OR, NOT,IN, BETWEEN, LIKE, NULL, LIMIT, ORDER, TOP.


-- 1. RETRIEVE ALL COLUMNS FROM BOTH TABLES
SELECT * FROM Customers
SELECT * FROM Orders


-- 2. Retrieve unique items from table
SELECT DISTINCT(item_name), * FROM Orders;


-- 3. Select orders where quantity is greater than average quantity
SELECT DISTINCT(item_name), *  FROM Orders WHERE quantity > (SELECT AVG(quantity) FROM Orders)


-- 4. Find Orders only for id 25, 27, 32, 40. Find orders where quantity is between 8 to 16
SELECT * FROM Orders WHERE order_id IN (25, 27, 32, 40, 107, 108, 110, 113)
SELECT * FROM Orders WHERE quantity BETWEEN 8 AND 16


-- 5. Find customers whose names:Start with R, End with a., Contain ee.
SELECT * FROM Customers WHERE 
customer_name LIKE 'R%'     
AND customer_name LIKE '%v' 
AND customer_name LIKE '%te%'
