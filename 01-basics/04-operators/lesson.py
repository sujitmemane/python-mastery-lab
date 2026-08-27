"""Lesson: arithmetic, comparison, logical, membership, and identity operators."""

print(7 + 2, 7 // 2, 7 % 2, 2 ** 3)  # Expected: 9 3 1 8
print(5 == 5, 5 != 3, 5 > 3)  # Expected: True True True
print(True and False, True or False, not True)  # Expected: False True False
print("py" in "python")  # Expected: True

first = [1, 2]
second = first
third = [1, 2]
print(first == third)  # Expected output: True; equal contents.
print(first is third)  # Expected output: False; different list objects.
print(first is second)  # Expected output: True; same object identity.

# Use == for equality and is for identity. Use `is None` for the singleton None.