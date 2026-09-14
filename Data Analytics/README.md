# End-to-End Data Analytics Curriculum & Projects

This module contains practical case studies, automated data cleaning engines, EDA frameworks, SQL profiling scripts, and analytical workflows for modern **Business Intelligence** and **Data Analytics**.

---

## 📚 Curriculum Roadmap

```mermaid
flowchart LR
    A["1. Defining Problem Statements"] --> B["2. Hypothesis & Question Formulation"]
    B --> C["3. Ingestion & Data Profiling"]
    C --> D["4. Automated Cleaning & Validation"]
    D --> E["5. Exploratory Data Analysis (EDA)"]
    E --> F["6. Business Dashboards & Reporting"]
```

### Module 1: Business Framing & Problem Articulation
* **Business Objective Identification**: Aligning project scope with organizational goals (revenue optimization, churn reduction, customer acquisition cost).
* **KPI Definition**: Revenue, Gross Margin, Average Order Value (AOV), Customer Lifetime Value (CLV), Retention Rates.
* **Formulating Impactful Questions**: Developing structured analytical questions to guide exploration.

### Module 2: Ingestion & Data Profiling
* Multi-source data extraction (SQL databases, CSVs, Excel, REST APIs).
* Structural audits: row counts, cardinality, schema types, missingness ratios.
* SQL profiling using conditional aggregations and system metadata procedures.

### Module 3: Data Cleaning & Automated Quality Assurance
* Handling missing values: conditional mean/median imputation, forward/backward fill for time series, mode for categories.
* Deduplication and data integrity constraints.
* Inconsistent categorical string normalization and date-time standardization.
* Reusable Python OOP engines (`AutoCleanEngine`).

### Module 4: Exploratory Data Analysis (EDA)
* **Univariate Analysis**: Histograms, kernel density estimates, skewness, kurtosis.
* **Outlier Detection**:
  * $Z$-Score methodology ($|Z| > 3$) for normally distributed features.
  * Interquartile Range (IQR: $[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$) for skewed data.
* **Bivariate & Multivariate Relationships**: Pearson and Spearman correlation matrices, cross-tabulations, feature interactions.

### Module 5: Reporting, Dashboards & Strategic Recommendations
* Interactive reporting with Streamlit, Power BI, and Tableau.
* Translating technical findings into executive business strategies.

---

## 📂 Repository Contents

| Directory / File | Description |
| :--- | :--- |
| [Fundamentals.txt](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/Data%20Analytics/Fundamentals.txt) | Core concepts, comparison with Data Science, 6-step lifecycle, and technology stack. |
| [1_Steps/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/Data%20Analytics/1_Steps) | Step-by-step guides from problem statement to final executive strategy. |
| [2_Data_Transformation/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/Data%20Analytics/2_Data_Transformation) | Data profiling, automated cleaning scripts (`auto_cleaning.py`), EDA engine (`_EDA_.py`), and case studies. |
| [3_Strategies/](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/Data%20Analytics/3_Strategies) | Analytical strategies, descriptive analysis, and Streamlit app (`Descriptive.py`). |
