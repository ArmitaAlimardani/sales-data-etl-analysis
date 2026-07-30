from datetime import date

CITIES = [
    "Tehran",
    "Mashhad",
    "Isfahan",
    "Shiraz",
    "Tabriz",
    "Karaj",
    "Ahvaz",
    "Qom",
    "Kermanshah",
    "Rasht"
]

PRODUCTS = {
    "Electronics": [
        ("Laptop", 1200),
        ("Smartphone", 800),
        ("Tablet", 500),
        ("Headphones", 150),
        ("Smart Watch", 250)
    ],
    "Home Appliances": [
        ("Vacuum Cleaner", 300),
        ("Microwave", 220),
        ("Refrigerator", 1800),
        ("Washing Machine", 1500),
        ("Air Conditioner", 2000)
    ],
    "Books": [
        ("Python Programming", 45),
        ("Data Science Handbook", 60),
        ("Clean Code", 55),
        ("Algorithms", 70),
        ("Machine Learning", 80)
    ],
    "Sports": [
        ("Football", 30),
        ("Basketball", 35),
        ("Tennis Racket", 180),
        ("Running Shoes", 120),
        ("Fitness Band", 90)
    ]
}

MIN_QUANTITY = 1
MAX_QUANTITY = 5

NUMBER_OF_ORDERS = 10000

START_DATE = date(2024, 1, 1)
END_DATE = date(2025, 12, 31)