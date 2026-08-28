"""Lesson: lists are ordered collections that can change."""

fruits = ["apple", "banana"]
fruits.append("cherry")
fruits[0] = "apricot"
print(fruits)
print(fruits[1:])

for fruit in fruits:
    print(fruit)