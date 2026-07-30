from pathlib import Path
import sqlite3

import pandas as pd


PROCESSED_DATA_PATH = Path("data/processed/cleaned_sales_data.csv")
DATABASE_PATH = Path("database/sales.db")
TABLE_NAME = "sales"


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


def load_processed_data():
    return pd.read_csv(PROCESSED_DATA_PATH)


def save_to_database(dataframe):
    with create_connection() as connection:
        dataframe.to_sql(
            TABLE_NAME,
            connection,
            if_exists="replace",
            index=False
        )


def main():
    dataframe = load_processed_data()
    save_to_database(dataframe)

    print(f"{len(dataframe)} rows saved to the database.")
    print(f"Database created at {DATABASE_PATH}")
    print(f"Table name: {TABLE_NAME}")


if __name__ == "__main__":
    main()