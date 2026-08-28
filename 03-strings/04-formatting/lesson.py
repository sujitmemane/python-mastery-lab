"""Lesson: f-strings put values into readable text."""

# Objective:
# Insert values and expressions into text, then control number formatting.

# Mental model:
# An f-string is a sentence template. Braces are slots evaluated at runtime.

name = "Mina"
age = 21
score = 0.875

print(f"{name} is {age} years old.")
# Result: Mina is 21 years old.

print(f"Score: {score:.1%}")
# Result: Score: 87.5%
# .1% means convert to a percentage and show one decimal place.

print(f"Next year, {name} will be {age + 1}.")
# Result: Next year, Mina will be 22.

price = 12.5
quantity = 3
print(f"Total: ${price * quantity:.2f}")
# Result: Total: $37.50

# Common mistake:
# print("Next year, {age + 1}") prints the braces literally because the
# string is not marked with the f prefix.

# Active recall:
# What does f"{score:.0%}" print for score = 0.875?
