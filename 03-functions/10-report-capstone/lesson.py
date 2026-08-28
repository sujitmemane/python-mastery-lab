"""Lesson: a useful program is a composition of focused functions.

Capstone goal: build a report pipeline with validation, transformation,
aggregation, and formatting. Keep data moving through return values.
"""

def valid_transaction(transaction):
    return transaction.get("amount", 0) >= 0 and bool(transaction.get("category"))


def total_for_category(transactions, category):
    return sum(
        item["amount"] for item in transactions
        if valid_transaction(item) and item["category"] == category
    )


transactions = [
    {"category": "food", "amount": 12.50},
    {"category": "travel", "amount": 30.00},
]
print(total_for_category(transactions, "food"))

# Design check: each function has one responsibility and no global accumulator.