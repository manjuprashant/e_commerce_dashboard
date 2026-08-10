# clean_ecommerce.py

import pandas as pd
import os

def load_and_clean(file_path, output_path="cleaned_ecommerce.csv"):
    """
    Load and clean the E-commerce dataset.
    Args:
        file_path (str): Path to the dataset file
        output_path (str): Path to save cleaned dataset
    """

    # Load dataset
    df = pd.read_csv(file_path, encoding="utf-8")

    # --- Cleaning steps ---
    # 1. Remove duplicate rows
    df = df.drop_duplicates()

    # 2. Handle missing values
    threshold = len(df) * 0.5
    df = df.dropna(thresh=threshold, axis=1)

    # Handle missing values safely
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
           df[col] = df[col].fillna(df[col].mean())
        else:
           df[col] = df[col].fillna(df[col].mode()[0])


    # 3. Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 4. Remove outliers (IQR method for numeric columns)
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {os.path.abspath(output_path)}")

if __name__ == "__main__":
    load_and_clean(r"C:\Users\smanj\Downloads\SPRINGER CAPITAL\E-Commerce Dashboard\SuperStore_Sales_Dataset.csv")
