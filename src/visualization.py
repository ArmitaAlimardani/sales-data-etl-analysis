from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


DATABASE_PATH = Path("database/sales.db")
FIGURES_PATH = Path("reports/figures")


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


def load_sales_by_category():
    query = """
        SELECT category, SUM(total_price) AS total_sales
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    """

    with create_connection() as connection:
        return pd.read_sql_query(query, connection)

def load_sales_by_city():
    query = """
        SELECT city, SUM(total_price) AS total_sales
        FROM sales
        GROUP BY city
        ORDER BY total_sales DESC
    """

    with create_connection() as connection:
        return pd.read_sql_query(query, connection)


def load_top_products():
    query = """
        SELECT product, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 5
    """

    with create_connection() as connection:
        return pd.read_sql_query(query, connection)


def create_sales_by_category_chart(dataframe):
    FIGURES_PATH.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(dataframe["category"], dataframe["total_sales"])
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=20)
    plt.tight_layout()

    output_path = FIGURES_PATH / "sales_by_category.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to {output_path}")

def create_sales_by_city_chart(dataframe):
    plt.figure(figsize=(10, 6))
    plt.bar(dataframe["city"], dataframe["total_sales"])
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=30)
    plt.tight_layout()

    output_path = FIGURES_PATH / "sales_by_city.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to {output_path}")


def create_category_pie_chart(dataframe):
    plt.figure(figsize=(8, 8))
    plt.pie(
        dataframe["total_sales"],
        labels=dataframe["category"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Sales Share by Category")

    output_path = FIGURES_PATH / "category_share.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to {output_path}")


def create_top_products_chart(dataframe):
    plt.figure(figsize=(10, 6))
    plt.barh(dataframe["product"], dataframe["total_quantity"])
    plt.title("Top 5 Products")
    plt.xlabel("Units Sold")
    plt.tight_layout()

    output_path = FIGURES_PATH / "top_products.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to {output_path}")


def main():
    sales_by_category = load_sales_by_category()
    sales_by_city = load_sales_by_city()
    top_products = load_top_products()

    create_sales_by_category_chart(sales_by_category)
    create_sales_by_city_chart(sales_by_city)
    create_category_pie_chart(sales_by_category)
    create_top_products_chart(top_products)


if __name__ == "__main__":
    main()