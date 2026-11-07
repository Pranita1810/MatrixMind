--- DDL TASKS ---

-- **Build E-Commerce database**
-- 1. Customers + Orders
-- 2. Build Relation between tables
-- 3. If parent deleted, it should delete child row too.
-- 4. Ensure there should be no duplicate Values




------------ SSMS ------------
CREATE TABLE Customer_Info(
    customer_id BIGINT PRIMARY KEY IDENTITY(1,1),
    customer_name VARCHAR(50) NULL,
    email VARCHAR(30) UNIQUE,
    phone BIGINT UNIQUE,   
)

CREATE TABLE Order_Info(
    order_id BIGINT PRIMARY KEY IDENTITY(1,1),
    customer_id BIGINT NOT NULL,
    order_date DATE,
    item_name VARCHAR(100) NULL,
    price DECIMAL(5,2),
    quantity INT,
    FOREIGN KEY(customer_id) REFERENCES Customer_Info(customer_id)
    ON DELETE CASCADE
)



------------ PG ------------
CREATE TABLE Customer_Info(
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_name VARCHAR(50) NULL,
    email VARCHAR(30) UNIQUE,
    phone BIGINT UNIQUE   
);

CREATE TABLE Order_Info(
    order_id BIGINT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    order_date DATE,
    item_name VARCHAR(100) NULL,
    price DECIMAL(5,2),
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES Customer_Info(customer_id)
    ON DELETE CASCADE
);



--########################################################################################################################################################################################################################################################################

---- DDL TASKS LEVEL 2 ----

-- **MODIFICATION IN TABLE**
-- 1. Add customer_status VARCHAR(20) with default 'Active'.
-- 2. Change customer_name from VARCHAR(50) to VARCHAR(100).
-- 3. Rename phone to phone_number.
-- 4. Add a CHECK constraint ensuring price > 0.
-- 5. Add a CHECK constraint ensuring quantity > 0.
-- 6. Add a UNIQUE constraint on (customer_id, item_name, order_date).
-- 7. Remove the UNIQUE constraint on phone_number.
-- 8. Change the foreign key from ON DELETE CASCADE to ON DELETE SET NULL. Handle the NOT NULL conflict.
-- 9. Add an index on Order_Info(customer_id, order_date).
-- 10. Rename Customer_Info to Customers and Order_Info to Orders.


--- SSMS ---
ALTER TABLE Customer_Info ADD customer_status VARCHAR(20) DEFAULT 'Active'
ALTER TABLE Customer_Info ALTER COLUMN customer_name VARCHAR(100)
EXEC sp_rename 'Customer_Info.phone', 'phone_number', 'COLUMN'
ALTER TABLE Order_Info ADD CONSTRAINT chk_price CHECK (price >=0)
ALTER TABLE Order_Info ADD CONSTRAINT chk_qt CHECK (quantity > = 0)
ALTER TABLE Order_Info ADD CONSTRAINT chk_uq UNIQUE (customer_id, item_name, order_date)
ALTER TABLE Customer_Info DROP CONSTRAINT UQ__Customer__B43B145F722B7248
ALTER TABLE Order_Info DROP CONSTRAINT chk_uq
ALTER TABLE Order_Info DROP CONSTRAINT FK__Order_Inf__custo__73BA3083
ALTER TABLE Order_Info ALTER COLUMN customer_id BIGINT NULL
ALTER TABLE Order_Info ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES Customer_Info(customer_id) ON DELETE SET NULL
CREATE INDEX idx_order_customer_id ON Order_Info(customer_id, order_id) 
EXEC sp_rename 'Customer_Info', 'Customers'
EXEC sp_rename 'Order_Info', 'Orders'
EXEC sp_rename 'Customers', 'Customer_Info'
EXEC sp_rename 'Orders', 'Order_Info'



--- PG ---
ALTER TABLE Customer_Info ADD COLUMN Customer_Status VARCHAR(10)  DEFAULT 'Active'
ALTER TABLE Customer_Info ALTER COLUMN customer_name TYPE VARCHAR(100)
ALTER TABLE Customer_Info RENAME COLUMN  phone TO phone_numer
ALTER TABLE Order_Info ADD CONSTRAINT price_chk CHECK (price>0)
ALTER TABLE Order_Info ADD CONSTRAINT qt_chk CHECK (quantity>0)
ALTER TABLE Order_Info ADD CONSTRAINT chk_uq_id UNIQUE (customer_id, order_id)
ALTER TABLE Customer_Info DROP COLUMN phone_numer
ALTER TABLE Customer_Info ADD COLUMN phone_number VARCHAR(15)
ALTER TABLE Order_Info DROP COLUMN customer_id
ALTER TABLE Order_Info ADD COLUMN customer_id  BIGINT
ALTER TABLE Order_Info ADD CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES Customer_Info(customer_id) ON DELETE SET NULL
CREATE INDEX idx_id_date ON Order_Info(order_id, order_date)
ALTER TABLE Customer_Info RENAME to Customers
ALTER TABLE Order_Info RENAME TO Orders

SELECT * FROM Orders;
SELECT * FROM Customers;