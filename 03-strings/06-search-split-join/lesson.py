"""Lesson: search methods inspect text; split and join change its shape.

Objective: test for patterns and move between a string and a list of pieces.
Mental model: `split` cuts at separators, while `join` uses one separator to
assemble pieces. `find` reports a position; `in` answers membership.
"""

email = "ada@example.com"
print("@" in email)
# Result: True
print(email.find("@"))
# Result: 3
print(email.startswith("ada"), email.endswith(".com"))
# Result: True True

parts = "red,green,blue".split(",")
print(parts)
# Result: ['red', 'green', 'blue']
print(" | ".join(parts))
# Result: red | green | blue
print("  learn   Python\n every day ".split())
# Result: ['learn', 'Python', 'every', 'day']

# Common mistake:
# `find()` returns -1 when text is absent. `index()` raises ValueError instead.

# Active recall: why is `"-".join(parts)` valid, but `parts.join("-")` not?