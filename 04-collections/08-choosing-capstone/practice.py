"""Capstone: build an order analyzer and justify each collection choice."""

# Use this data, but decide the collection type for each result yourself.
orders = [
    {"customer": "Ava", "product": "pen", "quantity": 2, "price": 3.0},
    {"customer": "Mia", "product": "book", "quantity": 1, "price": 12.0},
    {"customer": "Ava", "product": "book", "quantity": 2, "price": 12.0},
]

# Required results:
# - unique customers
# - total revenue by product
# - products purchased by both Ava and Mia
# - the highest-value order
# Challenge: handle [] and use at least one comprehension after first writing
# the loop version. Write a short justification for every result's structure.