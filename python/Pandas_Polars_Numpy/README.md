# High-Performance Data Engineering: NumPy, Pandas, Polars & Project

This folder contains core references, notebook experiments, and a production-grade ETL project comparing and integrating **NumPy**, **Pandas**, and **Polars**.

---

## 📚 Comparative Overview

| Feature | NumPy | Pandas | Polars |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | N-Dimensional Numeric Arrays | Tabular Data Analysis (Single-Core) | High-Performance DataFrames |
| **Underlying Language** | C / Fortran | C / Python (built on NumPy) | Rust (built on Apache Arrow) |
| **Parallel Execution** | Limited (BLAS/LAPACK) | Single-threaded (GIL-bound) | Fully Multi-Threaded across all cores |
| **Execution Paradigm** | Eager | Eager | Both Eager and Lazy (`LazyFrame`) |
| **Memory Model** | C contiguous blocks | NumPy blocks | Arrow columnar format (Zero-copy) |
| **Ideal Use Case** | Linear algebra, ML tensor math | Exploratory analysis, small-to-mid datasets | Large-scale ETL, memory-constrained data |

---

## 📂 Subdirectories & Modules

| Module | Description |
| :--- | :--- |
| [Numpy/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Numpy) | Vectorization, broadcasting rules, array slicing, and [study.ipynb](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Numpy/study.ipynb). |
| [Pandas/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Pandas) | Series, DataFrames, indexing, aggregations, and [Pandas_main.ipynb](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Pandas/Pandas_main.ipynb). |
| [Polars/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Polars) | Rust-powered DataFrames, expressions, lazy planning, and [polars_.ipynb](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/Polars/polars_.ipynb). |
| [PROJECT/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/Pandas_Polars_Numpy/PROJECT) | End-to-End Hybrid ETL Pipeline connecting MS SQL Server with Polars transformations and Parquet storage. |
