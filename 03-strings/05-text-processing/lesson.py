"""Lesson: strings are immutable, so transformations return new strings.

Objective: compose transformations while preserving the source text.
Mental model: each operation creates a new value; it does not edit the
characters inside the existing string.
"""

text = "Python"
upper_text = text.upper()
print(text)
print(upper_text)

# text[0] = "p" would raise TypeError. Build a new string instead.
changed_text = "p" + text[1:]
print(changed_text)

line = "Python makes text processing practical"
words = line.lower().split()
print(len(words))
print(" ".join(words))

print("ABC123".isalnum())
print("123".isdigit())
print("hello".isalpha())

# Active recall: what happens if `text.upper()` is called but not stored?
