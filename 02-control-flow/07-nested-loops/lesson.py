"""Lesson: put one loop inside another loop."""

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})")

# The outer loop chooses the row. For each row, the inner loop visits
# every column before the outer loop moves to the next row.

for row in range(1, 4):
    line = ""
    for column in range(1, 4):
        line += "* "
    print(line)
