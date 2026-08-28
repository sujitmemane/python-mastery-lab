"""Solutions for nested-data practice."""

users = [{"name": "Ava", "roles": ["reader"]}, {"name": "Mia", "roles": ["admin"]}]
for user in users:
    print(user["name"])
for user in users:
    if "admin" in user["roles"]:
        print(user["name"])

orders = [
    {"items": [{"product": "pen", "quantity": 2}, {"product": "book", "quantity": 1}]},
    {"items": [{"product": "pen", "quantity": 3}]},
]
totals = {}
for order in orders:
    for item in order["items"]:
        product = item["product"]
        totals[product] = totals.get(product, 0) + item["quantity"]
print(totals)