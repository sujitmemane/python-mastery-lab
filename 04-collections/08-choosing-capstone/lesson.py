"""Lesson: choose a collection by asking what operations the data needs.

Objective: justify a structure rather than memorizing a one-to-one rule.
"""

recent_events = ["login", "view", "login"]  # ordered history; duplicates matter
roles = {"reader", "editor"}  # unique membership
coordinates = (40.7, -74.0)  # fixed record
settings = {"timeout": 30, "retries": 3}  # key-based lookup

print(recent_events)
print("editor" in roles)
print(coordinates)
print(settings["timeout"])

# Active recall: what requirement would make a list a better choice than a set?