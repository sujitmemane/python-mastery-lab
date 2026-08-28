"""Practice: process nested, API-like data."""

# Level 1 - Print each user's name from this list of dictionaries.
users = [{"name": "Ava", "roles": ["reader"]}, {"name": "Mia", "roles": ["admin"]}]

# Level 2 - Print users whose roles contain "admin".

# Level 3 - Count total quantities by product across all orders.
orders = [
    {"items": [{"product": "pen", "quantity": 2}, {"product": "book", "quantity": 1}]},
    {"items": [{"product": "pen", "quantity": 3}]},
]

# Level 4 - Return an empty dictionary for empty orders and explain why
# product totals need a dictionary rather than a set.