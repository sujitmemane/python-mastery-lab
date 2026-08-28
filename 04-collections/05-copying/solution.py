"""Solutions for copying practice."""

items = ["one"]
same_items = items
same_items.append("two")
print(items)

independent = items.copy()
independent.append("three")
print(items)
print(independent)

from copy import deepcopy

matrix = [[1, 2], [3, 4]]
matrix_copy = deepcopy(matrix)
matrix_copy[0][0] = 99
print(matrix)
print(matrix_copy)