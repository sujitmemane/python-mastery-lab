"""Practice: use nested loops for repeated groups."""

# Level 1 - Print a 3 by 4 rectangle of stars.
for row in range(3):
    for column in range(4):
        pass


# Level 2 - Print this right triangle:
# *
# * *
# * * *
for row in range(1, 4):
    pass


# Level 3 - Print a multiplication table from 1 x 1 through 3 x 3.
for first in range(1, 4):
    for second in range(1, 4):
        pass


# Level 4 - Count how many pairs have the same value.
values = [1, 2, 1, 3]
matching_pairs = 0
for first_index in range(len(values)):
    for second_index in range(first_index + 1, len(values)):
        pass
print(matching_pairs)
