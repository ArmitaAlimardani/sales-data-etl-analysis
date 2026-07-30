import random
import pandas as pd

from faker import Faker

from constants import (
    CITIES,
    PRODUCTS,
    MIN_QUANTITY,
    MAX_QUANTITY,
    NUMBER_OF_ORDERS,
    START_DATE,
    END_DATE,
)


fake = Faker()


def generate_order():
    category = random.choice(list(PRODUCTS.keys()))
    product, unit_price = random.choice(PRODUCTS[category])
    quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)

    order = {
        "customer_name": fake.name(),
        "city": random.choice(CITIES),
        "category": category,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": quantity * unit_price,
        "order_date": fake.date_between(
            start_date=START_DATE,
            end_date=END_DATE
        )
    }

    return order

def generate_dataset():
    orders = []

    for order_id in range(1, NUMBER_OF_ORDERS + 1):
        order = generate_order()
        order["order_id"] = order_id
        orders.append(order)

    return orders


def save_to_csv(orders):
    dataframe = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "order_date",
        "customer_name",
        "city",
        "category",
        "product",
        "quantity",
        "unit_price",
        "total_price"
    ]
)
    dataframe.to_csv(
        "data/raw/sales_data.csv",
        index=False
    )


def main():
    orders = generate_dataset()
    save_to_csv(orders)

    print(f"{len(orders)} orders generated successfully.")
    print("File saved to data/raw/sales_data.csv")


if __name__ == "__main__":
    main()