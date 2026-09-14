---- DATA PROFILING QUERIES (T-SQL) ----

-- 1. Total Record Count
SELECT COUNT(*) AS total_rows 
FROM test.dbo.dirty_cafe_sales;

-- 2. Inspect Sample Data
SELECT TOP 100 * 
FROM test.dbo.dirty_cafe_sales;

-- 3. Comprehensive Null Value Audit Across Key Columns
SELECT 
    SUM(CASE WHEN Transaction_Date IS NULL THEN 1 ELSE 0 END) AS null_transaction_date,
    SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END)         AS null_quantity,
    SUM(CASE WHEN Item IS NULL THEN 1 ELSE 0 END)             AS null_item,
    SUM(CASE WHEN Price_Per_Unit IS NULL THEN 1 ELSE 0 END)   AS null_price_per_unit,
    SUM(CASE WHEN Total_Spent IS NULL THEN 1 ELSE 0 END)      AS null_total_spent
FROM test.dbo.dirty_cafe_sales;

-- 4. Check Schema & Column Data Types
EXEC sp_help 'test.dbo.dirty_cafe_sales';
