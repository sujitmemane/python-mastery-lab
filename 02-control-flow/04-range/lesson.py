"""Lesson: generate a sequence of integers with range()."""

for number in range(5):
    print(number)

# Expected output: 0, 1, 2, 3, 4.
# The stop value, 5, is excluded.

print(list(range(2, 6)))  # Expected output: [2, 3, 4, 5]
print(list(range(2, 10, 2)))  # Expected output: [2, 4, 6, 8]

# range(start, stop, step): start is included, stop is excluded.
# range is useful when you need repetition based on positions or counts.
for index in range(len(["a", "b", "c"])):
    print(index)