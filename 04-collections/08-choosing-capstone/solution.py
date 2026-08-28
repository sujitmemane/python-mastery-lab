"""Reference solution for the collection-choice capstone."""

orders = [
    {"customer": "Ava", "product": "pen", "quantity": 2, "price": 3.0},
    {"customer": "Mia", "product": "book", "quantity": 1, "price": 12.0},
    {"customer": "Ava", "product": "book", "quantity": 2, "price": 12.0},
]

customers = {order["customer"] for order in orders}
revenue = {}
products_by_customer = {}
for order in orders:
    value = order["quantity"] * order["price"]
    revenue[order["product"]] = revenue.get(order["product"], 0) + value
    products_by_customer.setdefault(order["customer"], set()).add(order["product"])

shared_products = products_by_customer.get("Ava", set()) & products_by_customer.get("Mia", set())
highest_order = max(orders, key=lambda order: order["quantity"] * order["price"], default=None)
print(customers)
print(revenue)
print(shared_products)
print(highest_order)