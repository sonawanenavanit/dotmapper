import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/support_tickets.csv")


def load_csv():
    try:
        df = pd.read_csv(DATA_PATH)

        # Convert date column
        df["created_at"] = pd.to_datetime(df["created_at"])

        print("=" * 50)
        print("Dataset Loaded Successfully")
        print("=" * 50)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        return df

    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None


if __name__ == "__main__":
    df = load_csv()

    if df is not None:
        print("\nFirst Five Rows:")
        print(df.head())