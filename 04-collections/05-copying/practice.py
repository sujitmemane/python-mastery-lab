"""Practice: predict and control shared references."""

# Level 1 - Predict what prints, then explain why.
items = ["one"]
same_items = items
same_items.append("two")
print(items)

# Level 2 - Make independent a copy, then append "three" to it.
independent = items

# Level 3 - Copy this nested list and change only the copy's first value.
matrix = [[1, 2], [3, 4]]

# Level 4 - Explain in a comment why a shallow copy is not enough for matrix.