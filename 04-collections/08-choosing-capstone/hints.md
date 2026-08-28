# Hints

1. Customer uniqueness suggests a set; product totals suggest a dictionary.
2. Compute each order value as `quantity * price`.
3. Build one product set per customer and intersect them.
4. For empty input, choose a documented result such as `None` for no highest order.