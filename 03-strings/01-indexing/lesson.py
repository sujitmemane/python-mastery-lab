"""Lesson: strings are ordered sequences of characters."""

word = "Python"
print(word[0])
print(word[-1])
print(len(word))

# Indexing starts at zero. Negative indexes count from the end.
for index in range(len(word)):
    print(index, word[index])
