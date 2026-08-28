"""Lesson: nested collections model records such as API or JSON data.

Objective: read and aggregate a list of dictionaries without losing track of
which level is being accessed. Mental model: each value is a container inside
another container; inspect one layer at a time.
"""

orders = [
    {"customer": "Ava", "items": [{"name": "pen", "quantity": 2}]},
    {"customer": "Mia", "items": [{"name": "book", "quantity": 1}]},
]

for order in orders:
    for item in order["items"]:
        print(order["customer"], item["name"], item["quantity"])

# Active recall: which brackets access the order, and which access its item?