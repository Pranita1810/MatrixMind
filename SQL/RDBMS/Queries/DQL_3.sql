----- * ADVANCED DQL * -----

-- 1. Find customers whose customer_id exists in the order_info table..
SELECT customer_id FROM customer_info 
WHERE customer_id IN (SELECT customer_id FROM order_info )

-- 2. Find cusotmer whose total order vlaue is greater than the average total order value per cusotmer.
SELECT C.customer_id, C.first_name,
       SUM(OI.list_price * OI.quantity) AS total_value
FROM customer_info C
JOIN order_info O
    ON C.customer_id = O.customer_id
JOIN order_item_info OI
    ON O.order_id = OI.order_id
GROUP BY C.customer_id, C.first_name
HAVING SUM(OI.list_price * OI.quantity) >
(
    SELECT AVG(customer_total)
    FROM (
        SELECT O2.customer_id,
               SUM(OI2.list_price * OI2.quantity) AS customer_total
        FROM order_info O2
        JOIN order_item_info OI2
            ON O2.order_id = OI2.order_id
        GROUP BY O2.customer_id
    ) AS T
);


--3. Find customers who have placed at least one order with a total order value greater than ₹10,000.
SELECT C.customer_id, C.first_name, SUM(OI.list_price*OI.quantity) FROM 
customer_info C JOIN order_info O ON C.customer_id=O.customer_id
JOIN order_item_info OI ON OI.order_id=O.order_id
GROUP BY C.customer_id, C.first_name
HAVING SUM(OI.list_price*OI.quantity) > 10000



-- 4. UNION & UNION ALL Combine all customer and staff first names, removing duplicates.
SELECT  first_name FROM customer_info
UNION 
SELECT  first_name FROM staff_info


-- 5. Combine customer IDs from order_info and customer_info, retaining duplicates.
SELECT customer_id FROM customer_info
UNION ALL 
SELECT customer_id FROM order_info



-- 6. Common Table Expression 
WITH TempTable AS (
    SELECT * FROM customer_info
)
SELECT * FROM TempTable


-- 7. Find customers who have placed at least 3 orders & have total spending more than 50k
WITH customers AS (
    SELECT C.customer_id , C.first_name, SUM(OI.list_price) AS total_value, COUNT(C.customer_id) AS purchase_count
    FROM customer_info C JOIN order_info O ON C.customer_id=O.customer_id
    JOIN order_item_info OI ON OI.order_id=O.order_id
    GROUP BY C.customer_id, C.first_name
)
SELECT * FROM customers WHERE total_value > 10000 AND purchase_count > 3


-- 8. WINDOWS FUNCTIONS
SELECT item_id, order_id, list_price ,
ROW_NUMBER() OVER(ORDER BY list_price DESC) AS ROW_NUMBER,
RANK() OVER(ORDER BY list_price DESC) AS rank_,
DENSE_RANK() OVER(ORDER BY list_price DESC) AS d_rank
FROM order_item_info


-- 9. Using customer info and order info : Find each customer's total number of orders, rank customers by total order
WITH custom_table AS (
SELECT C.customer_id, C.first_name, COUNT(O.customer_id) AS total_orders
FROM customer_info C LEFT JOIN order_info O ON C.customer_id=O.customer_id
GROUP BY C.customer_id, C.first_name)
SELECT *, 
RANK() OVER(ORDER BY total_orders) AS rank_, 
DENSE_RANK() OVER(ORDER BY total_orders) AS dense_rank_
 FROM custom_table
