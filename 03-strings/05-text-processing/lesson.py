"""Lesson: strings are immutable, so transformations return new strings.

Objective: compose transformations while preserving the source text.
Mental model: each operation creates a new value; it does not edit the
characters inside the existing string.
"""

text = "Python"
upper_text = text.upper()
print(text)
# Result: Python
print(upper_text)
# Result: PYTHON

# text[0] = "p" would raise TypeError. Build a new string instead.
changed_text = "p" + text[1:]
print(changed_text)
# Result: python

line = "Python makes text processing practical"
words = line.lower().split()
print(len(words))
# Result: 5
print(" ".join(words))
# Result: python makes text processing practical

print("ABC123".isalnum())
print("123".isdigit())
print("hello".isalpha())

# Common mistake:
# text.upper() by itself calculates a new string and then discards it. Store
# the result or use it immediately.

# Active recall: what happens if `text.upper()` is called but not stored?
