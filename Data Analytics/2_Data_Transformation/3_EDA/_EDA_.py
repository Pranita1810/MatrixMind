# -- Exploratory Data Analysis (EDA) --
# EDA is a foundational phase in data analytics and data science where analysts examine patterns,
# assess distributions, detect anomalies/outliers, and calculate feature correlations.

# -- CORE EDA TYPES --
# 1. Univariate analysis: Single variable analysis (distributions, summary statistics, histograms).
# 2. Bivariate analysis: Two variables (scatter plots, correlations, cross-tabulations).
# 3. Multivariate analysis: Three or more variables (pair plots, PCA, multi-variable interactions).

from scipy import stats
import pandas as pd 

# - Sample Dataset -
df = pd.DataFrame({
    "Name": ["Pranit", "Nigesh", "Lawrence", "Harsh", "Hemant"], 
    "Age": [22, 5, 12, 23, 43],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Testo": [800, 200, 100, 600, 690]
})

# - Skewness Detection -
# Skewness = 0: symmetric / normal; > 0: right-skewed; < 0: left-skewed
skewness_measure = stats.skew(df["Age"])

# - Outlier Detection Methods -
# 1. Z-Score: Identifies points beyond |Z| > 3 standard deviations from the mean
df["Age_zscore"] = stats.zscore(df["Age"])

# 2. Interquartile Range (IQR): Robust against non-normal distributions
Q1 = df["Testo"].quantile(0.25)
Q3 = df["Testo"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# - Correlation Matrix -
# +1: Perfect positive | +0.7 to +1: Strong positive | 0: No linear relation | -0.7 to -1: Strong negative | -1: Perfect negative
correlations = df.corr(numeric_only=True)


# ---- MODULAR EDA ENGINE ----
class EDAEngine:
    """Production-ready exploratory data analysis utility class."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    # Distribution analysis
    def get_skewness(self, column: str) -> float:
        return float(stats.skew(self.df[column].dropna()))

    # Outlier detection
    def detect_outliers(self, column: str, method: str = "IQR") -> pd.DataFrame:
        if method.upper() == "Z-SCORE":
            z_scores = stats.zscore(self.df[column].dropna())
            outlier_mask = abs(z_scores) > 3
            return self.df.loc[outlier_mask.index[outlier_mask]]

        elif method.upper() == "IQR":
            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            return self.df[(self.df[column] < lower) | (self.df[column] > upper)]
        else:
            raise ValueError("Method must be 'IQR' or 'Z-SCORE'")

    # Correlation analysis
    def get_correlation_matrix(self) -> pd.DataFrame:
        return self.df.corr(numeric_only=True)


if __name__ == "__main__":
    eda = EDAEngine(df)
    print("Detected Outliers (Age via Z-Score):")
    print(eda.detect_outliers("Age", method="Z-SCORE"))
    print("\nCorrelation Matrix:")
    print(eda.get_correlation_matrix())