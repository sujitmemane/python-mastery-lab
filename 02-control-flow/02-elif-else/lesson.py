"""Lesson: choose one result from multiple conditions."""

score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "Needs practice"

print(grade)  # Expected output: B

# Python checks from top to bottom and runs only the first matching branch.
# `else` runs when no preceding condition is true.

age = 12
if age < 13:
    group = "child"
elif age < 18:
    group = "teenager"
else:
    group = "adult"

print(group)  # Expected output: child