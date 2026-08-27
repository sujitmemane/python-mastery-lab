"""Lesson: common built-in data types."""

whole_number = 7
decimal_number = 2.5
complex_number = 2 + 3j
message = "Python"
is_ready = True
missing_value = None

for value in (whole_number, decimal_number, complex_number, message, is_ready, missing_value):
    print(type(value).__name__)

# Expected output: int, float, complex, str, bool, NoneType.
# `type` describes the object's exact type; isinstance also handles inheritance.
print(isinstance(whole_number, int))  # Expected output: True
print(isinstance(is_ready, int))  # Expected output: True; bool is a subclass of int.