"""Lesson: functions are objects, so they can be stored and passed around.

Objective: pass behavior into a reusable function and choose a clear style.
Mental model: a function name is a label for a callable value.
Real-world use: sorting, validation pipelines, and configurable services.
"""

def apply_twice(function, value):
    return function(function(value))


def add_one(number):
    return number + 1


print(apply_twice(add_one, 3))
print(sorted(["pear", "fig", "watermelon"], key=len))
print(list(filter(lambda number: number > 3, [1, 4, 2, 7])))

# Active recall: why does `add_one` work as an argument without parentheses?