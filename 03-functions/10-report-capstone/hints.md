# Hints

1. Validate with `.get()` so missing keys do not crash the check.
2. Build a new list rather than removing items while iterating.
3. Start totals with `{}` and use `.get(category, 0)`.
4. Sort `totals.items()` and format each pair. Decide what empty output means.