"""Lesson: search methods inspect text; split and join change its shape.

Objective: test for patterns and move between a string and a list of pieces.
Mental model: `split` cuts at separators, while `join` uses one separator to
assemble pieces. `find` reports a position; `in` answers membership.
"""

email = "ada@example.com"
print("@" in email)
print(email.find("@"))
print(email.startswith("ada"), email.endswith(".com"))

parts = "red,green,blue".split(",")
print(parts)
print(" | ".join(parts))
print("  learn   Python\n every day ".split())

# Active recall: why is `"-".join(parts)` valid, but `parts.join("-")` not?