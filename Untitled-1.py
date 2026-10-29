properties = [
    {"id": 1, "name": "Modern Apartment", "price": 50000},
    {"id": 2, "name": "Family House", "price": 120000},
    {"id": 3, "name": "Luxury Villa", "price": 250000},
]

for property in properties:
    print(f"{property['name']} - ${property['price']}")