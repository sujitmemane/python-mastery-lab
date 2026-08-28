"""Solutions for comprehension practice."""

print([value * 2 for value in range(1, 6)])

values = [-2, 0, 3, -1, 5]
print([value for value in values if value > 0])

words = ["red", "blue", "green"]
print({word: word.upper() for word in words})

word = "Mississippi"
print({letter.lower() for letter in word})