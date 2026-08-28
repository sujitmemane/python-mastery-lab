"""Lesson: parameters let a function work with supplied values."""

def greet(name, punctuation="!"):
    print(f"Hello, {name}{punctuation}")


greet("Ava")
greet("Mia", ".")