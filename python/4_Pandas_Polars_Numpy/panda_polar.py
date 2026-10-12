# PANDAS & POLARS
import pandas as pd
import polars as pl


#1. Data loading & invistigation
import pandas as pd
import polars as pl

# Pandas
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_parquet("data.parquet")

df.head(5)
df.tail(5)
df.info()
df.describe()
df.shape
df.dtypes

# Polars
df = pl.read_csv("data.csv")
df = pl.read_excel("data.xlsx")  # Requires an Excel engine
df = pl.read_parquet("data.parquet")

df.head(5)
df.tail(5)
df.glimpse()                     # Schema and sample values
df.describe()
df.shape
df.schema
df.null_count()


#------------------------------------------------------------------------------------

#2. Data selection & slicing
# Pandas
df["name"]
df[["name", "age"]]
df.loc[0:5, ["name", "age"]]
df.iloc[0:5, 0:2]

# Polars
df["name"]
df.select(["name", "age"])
df.filter(pl.col("age") > 25)
df.slice(0, 5)
df.select(["name", "age"]).head(5)


#------------------------------------------------------------------------------------

#3. Filtering data
# Pandas
df[df["age"] > 25]
df[(df["status"] == "active") & (df["score"] >= 80)]
df[df["category"].isin(["Tech", "Finance"])]
df[df["name"].str.contains("John", case=False, na=False)]
df[df["salary"].between(50000, 100000)]

# Polars
df.filter(pl.col("age") > 25)
df.filter(
    (pl.col("status") == "active") &
    (pl.col("score") >= 80)
)
df.filter(pl.col("category").is_in(["Tech", "Finance"]))
df.filter(pl.col("name").str.contains("(?i)John"))
df.filter(pl.col("salary").is_between(50000, 100000))


#------------------------------------------------------------------------------------
#Data cleaning & null handling
# Pandas
df.isna().sum()
df.dropna(subset=["critical_col"])
df["age"] = df["age"].fillna(df["age"].median())
df.drop_duplicates(subset=["id"], keep="first")

# Polars
df.null_count()
df.drop_nulls(subset=["critical_col"])
df = df.with_columns(
    pl.col("age").fill_null(pl.col("age").median())
)
df.unique(subset=["id"], keep="first")

# Important: NaN and null are different in Polars.
# Use fill_nan() for floating-point NaN values.


#------------------------------------------------------------------------------------
#GroupBy Aggregation
# Pandas
df.groupby("department")["salary"].mean()

df.groupby("region").agg(
    total_sales=("sales", "sum"),
    avg_order=("sales", "mean"),
    orders=("order_id", "count")
)

# Polars
df.group_by("department").agg(
    pl.col("salary").mean()
)

df.group_by("region").agg(
    pl.col("sales").sum().alias("total_sales"),
    pl.col("sales").mean().alias("avg_order"),
    pl.col("order_id").count().alias("orders")
)


#------------------------------------------------------------------------------------
#Feature Engineering
# Pandas
df["total_cost"] = df["quantity"] * df["unit_price"]

df["tier"] = df["spend"].apply(
    lambda x: "High" if x > 1000 else "Standard"
)

# Polars
df = df.with_columns(
    (pl.col("quantity") * pl.col("unit_price")).alias("total_cost")
)

df = df.with_columns(
    pl.when(pl.col("spend") > 1000)
    .then(pl.lit("High"))
    .otherwise(pl.lit("Standard"))
    .alias("tier")
)

#------------------------------------------------------------------------------------

#Merging, joining & concatenation
# Pandas
df_merged = pd.merge(df1, df2, on="user_id", how="left")
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)

# Polars
df_merged = df1.join(df2, on="user_id", how="left")

# Stack rows (vertical concatenation)
df_concat = pl.concat([df1, df2], how="vertical")

# Stack columns horizontally
df_horizontal = pl.concat([df1, df2], how="horizontal")


#------------------------------------------------------------------------------------

#Date-time parsing & operations
# Pandas
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["year"] = df["timestamp"].dt.year
df["month"] = df["timestamp"].dt.month_name()
df["day_of_week"] = df["timestamp"].dt.day_name()

# Polars
df = df.with_columns(
    pl.col("timestamp").str.to_datetime(strict=False)
)

df = df.with_columns(
    pl.col("timestamp").dt.year().alias("year"),
    pl.col("timestamp").dt.strftime("%B").alias("month"),
    pl.col("timestamp").dt.strftime("%A").alias("day_of_week")
)
#------------------------------------------------------------------------------------

#sorting & Ranking
# Pandas
df.sort_values(by="revenue", ascending=False)
df.sort_values(by=["department", "salary"],
               ascending=[True, False])
df.nlargest(5, "salary")
df.nsmallest(5, "salary")

# Polars
df.sort("revenue", descending=True)
df.sort(
    ["department", "salary"],
    descending=[False, True]
)
df.top_k(5, by="salary")
df.bottom_k(5, by="salary")