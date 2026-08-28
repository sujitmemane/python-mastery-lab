"""Lesson: slicing extracts part of a sequence without changing it."""

# Objective:
# Use start, stop, and step to take a section of a string.

# Mental model:
# A slice is a window over a string: text[start:stop:step].
# The start position is included, but the stop position is excluded.

text = "Python programming"

# Example 1: take indexes 0 through 5.
print(text[0:6])
# Result: Python
# Index 6 is not included, so the slice stops before the space.

# Example 2: omit start to begin at the first character.
print(text[:6])
# Result: Python

# Example 3: omit stop to continue through the end.
print(text[7:])
# Result: programming

# Example 4: use a step of 2 to take every second character.
print(text[::2])
# Result: Pto rgamn

# Example 5: use a negative step to read from right to left.
print(text[::-1])
# Result: gnimmargorp nohtyP

# Slicing creates a new string. The original text is still unchanged.
print(text)
# Result: Python programming

# Common mistake:
# text[0:6] means "indexes 0, 1, 2, 3, 4, 5", not six characters
# starting at index 1. Python indexes start at zero.

# Active recall:
# What would text[7:11] print? Predict before testing it.
