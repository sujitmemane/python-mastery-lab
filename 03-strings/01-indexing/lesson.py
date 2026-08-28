"""Lesson: strings are ordered sequences of characters."""

# Objective:
# Read one character, find a string's length, and loop over its indexes.

# Mental model:
# Imagine a string as labeled boxes. The first box is index 0, and negative
# indexes count backward from the last box.

word = "Python"

# Example 1: indexes start at zero.
print(word[0])
# Result: P

print(word[1])
# Result: y

# Example 2: negative indexes start at the end.
print(word[-1])
# Result: n

print(len(word))
# Result: 6

# Example 3: range(len(word)) gives every valid index.
for index in range(len(word)):
    print(index, word[index])
# Result:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# Common mistake:
# word[6] raises IndexError because the valid indexes are 0 through 5.

# Active recall:
# Predict word[-3] before running it. Which character box does it select?
