from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/sales_data.csv")
PROCESSED_DATA_PATH = Path("data/processed/cleaned_sales_data.csv")


def extract_data():
    return pd.read_csv(RAW_DATA_PATH)


def transform_data(dataframe):
    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe = cleaned_dataframe.drop_duplicates()
    cleaned_dataframe = cleaned_dataframe.dropna()

    cleaned_dataframe["order_date"] = pd.to_datetime(
        cleaned_dataframe["order_date"]
    )

    cleaned_dataframe["quantity"] = cleaned_dataframe["quantity"].astype(int)
    cleaned_dataframe["unit_price"] = cleaned_dataframe["unit_price"].astype(float)
    cleaned_dataframe["total_price"] = (
        cleaned_dataframe["quantity"] * cleaned_dataframe["unit_price"]
    )

    cleaned_dataframe = cleaned_dataframe.sort_values("order_date")

    return cleaned_dataframe


def load_data(dataframe):
    dataframe.to_csv(PROCESSED_DATA_PATH, index=False)


def main():
    raw_dataframe = extract_data()
    cleaned_dataframe = transform_data(raw_dataframe)
    load_data(cleaned_dataframe)

    print(f"Raw rows: {len(raw_dataframe)}")
    print(f"Cleaned rows: {len(cleaned_dataframe)}")
    print(f"Processed file saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()