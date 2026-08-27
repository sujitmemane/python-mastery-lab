"""Lesson: repeat a block once for every item in an iterable."""

names = ["Asha", "Ravi", "Mina"]

for name in names:
    print(f"Hello, {name}!")

# Expected output:
# Hello, Asha!
# Hello, Ravi!
# Hello, Mina!
#
# Trace:
# Pass 1 -> name is "Asha"
# Pass 2 -> name is "Ravi"
# Pass 3 -> name is "Mina"
# The indented block runs once for each item.

word = "cat"
for letter in word:
    print(letter)

# A string is iterable too, so the loop visits c, then a, then t.