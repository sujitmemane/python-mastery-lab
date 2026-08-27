"""Lesson: use if to run code only when a condition is true."""

temperature = 32

if temperature > 30:
    print("It is warm.")

# Python evaluates the condition first. Since 32 > 30 is True,
# the indented block runs. Indentation defines the block.

has_ticket = True
if has_ticket:
    print("You may enter.")  # Expected output: You may enter.

# A condition can combine comparisons with logical operators.
age = 20
has_id = True
if age >= 18 and has_id:
    print("Access approved.")  # Expected output: Access approved.