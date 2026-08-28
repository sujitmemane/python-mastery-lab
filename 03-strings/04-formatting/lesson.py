"""Lesson: f-strings put values into readable text."""

name = "Mina"
age = 21
score = 0.875

print(f"{name} is {age} years old.")
print(f"Score: {score:.1%}")
print(f"Next year, {name} will be {age + 1}.")

# Expressions inside braces are evaluated before the string is printed.
