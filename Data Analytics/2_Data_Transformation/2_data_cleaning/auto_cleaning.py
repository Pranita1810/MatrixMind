# ---- PRODUCTION READY AUTO DATA CLEANING ENGINE ----
import os
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype

class AutoCleanEngine:
    def __init__(self, path, file_type="csv"):
        self.path = path
        # - Excel Type -
        if file_type.lower() in ("xl", "xlsx", "xls"):
            self.df = pd.read_excel(path)
        # - CSV Type - 
        elif file_type.lower() == "csv":
            self.df = pd.read_csv(path, encoding="latin1")
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    # -- Remove Duplicates --
    def rm_duplicates(self):
        total_dups = self.df.duplicated().sum()
        if total_dups == 0:
            print("Zero duplicate rows found.")
        else:
            print(f"Removing {total_dups} duplicate rows...")
            self.df = self.df.drop_duplicates()
        return self.df

    # Backward compatibility alias
    def rm_dublicates(self):
        return self.rm_duplicates()

    # -- Handle Missing Values --
    def missing_val(self):
        for col in self.df.columns:
            if self.df[col].isna().sum() == 0:
                continue

            # - Numeric -
            if is_numeric_dtype(self.df[col]):
                # Impute with mean if approximately symmetric, else interpolate
                if abs(self.df[col].skew()) < 1:
                    self.df[col] = self.df[col].fillna(self.df[col].mean())
                else:
                    self.df[col] = self.df[col].interpolate()

            # - Datetime -
            elif is_datetime64_any_dtype(self.df[col]):
                self.df[col] = self.df[col].ffill()

            # - Text / Categorical -
            else:
                # Attempt conversion to datetime if >90% can parse
                temp = pd.to_datetime(self.df[col], errors="coerce")
                if temp.notna().mean() > 0.90:
                    self.df[col] = temp.ffill()
                else:
                    # Impute with mode for categorical columns
                    mode = self.df[col].mode()
                    if not mode.empty:
                        self.df[col] = self.df[col].fillna(mode[0])

        return self.df


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_path = os.path.join(current_dir, "case_study", "dirty_cafe_sales.csv")
    if os.path.exists(sample_path):
        cleaner = AutoCleanEngine(sample_path, "CSV")
        cleaner.rm_duplicates()
        cleaned_df = cleaner.missing_val()
        print(cleaned_df.head())
