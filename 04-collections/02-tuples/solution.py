"""Solutions for tuple practice."""

color = (32, 64, 128)
print(color)

book = ("Dune", "Frank Herbert", 1965)
title, author, year = book
print(f"{title} by {author} was published in {year}.")

left = "first"
right = "second"
left, right = right, left
print(left, right)

numbers = [4, 9, 1, 7]
print((min(numbers), max(numbers)))