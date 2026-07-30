from pathlib import Path
import sqlite3


DATABASE_PATH = Path("database/sales.db")


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


def execute_query(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def show_total_orders():
    query = """
        SELECT COUNT(*)
        FROM sales
    """

    result = execute_query(query)
    total_orders = result[0][0]

    print(f"Total Orders: {total_orders:,}")


def show_total_sales():
    query = """
        SELECT SUM(total_price)
        FROM sales
    """

    result = execute_query(query)
    total_sales = result[0][0]

    print(f"Total Sales: ${total_sales:,.2f}")


def show_average_order_value():
    query = """
        SELECT AVG(total_price)
        FROM sales
    """

    result = execute_query(query)
    average_order_value = result[0][0]

    print(f"Average Order Value: ${average_order_value:,.2f}")

def show_top_products():
    query = """
        SELECT product, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 5
    """

    results = execute_query(query)

    print("\nTop 5 Products:")
    for product, total_quantity in results:
        print(f"{product}: {total_quantity:,} units")


def show_sales_by_city():
    query = """
        SELECT city, SUM(total_price) AS total_sales
        FROM sales
        GROUP BY city
        ORDER BY total_sales DESC
    """

    results = execute_query(query)

    print("\nSales by City:")
    for city, total_sales in results:
        print(f"{city}: ${total_sales:,.2f}")


def show_sales_by_category():
    query = """
        SELECT category, SUM(total_price) AS total_sales
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    """

    results = execute_query(query)

    print("\nSales by Category:")
    for category, total_sales in results:
        print(f"{category}: ${total_sales:,.2f}")


def main():
    show_total_orders()
    show_total_sales()
    show_average_order_value()
    show_top_products()
    show_sales_by_city()
    show_sales_by_category()


if __name__ == "__main__":
    main()