"""Lesson: names, objects, assignment, and reassignment."""

# A variable name is a label that refers to an object.
score = 10
print(score)  # Expected output: 10

# Assignment can bind the same name to a different object.
score = 20
print(score)  # Expected output: 20

# Several names can be assigned in one statement.
first_name, age = "Sujit", 21
print(first_name, age)  # Expected output: Sujit 21

# Unpacking assigns items from a collection to separate names.
coordinates = (12, 8)
x_coordinate, y_coordinate = coordinates
print(x_coordinate, y_coordinate)  # Expected output: 12 8

# Two names can refer to the same mutable list.
tasks = ["learn"]
same_tasks = tasks
same_tasks.append("practice")
print(tasks)  # Expected output: ['learn', 'practice']

# Trace: tasks and same_tasks point to one list. append changes that list.
# Naming convention: use lowercase_with_underscores for variables.
# Constants are conventions, not enforced by Python: MAX_RETRIES = 3.