"""Reference solution for the transaction report capstone."""

def valid_transaction(record):
    return (
        isinstance(record.get("amount"), (int, float))
        and record["amount"] >= 0
        and bool(record.get("category"))
    )


def clean_transactions(records):
    return [record for record in records if valid_transaction(record)]


def total_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def format_report(totals):
    return "\n".join(
        f"{category}: ${amount:.2f}"
        for category, amount in sorted(totals.items())
    )


records = [
    {"category": "food", "amount": 12.50},
    {"category": "food", "amount": 7.50},
    {"category": "travel", "amount": 30},
    {"category": "broken", "amount": -1},
]
totals = total_by_category(clean_transactions(records))
print(format_report(totals))
assert totals == {"food": 20.0, "travel": 30}