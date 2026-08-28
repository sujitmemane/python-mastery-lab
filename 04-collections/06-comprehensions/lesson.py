"""Lesson: comprehensions build collections from an iterable."""

squares = [number * number for number in range(1, 5)]
even_squares = [number * number for number in range(1, 8) if number % 2 == 0]
lengths = {word: len(word) for word in ["cat", "python"]}
print(squares)
print(even_squares)
print(lengths)