"""Lesson: explicitly converting values between common types."""

age_text = "21"
age = int(age_text)
height = float("1.75")
label = str(404)
has_items = bool(["book"])

print(age + 1)  # Expected output: 22
print(height, label, has_items)  # Expected output: 1.75 404 True

# Conversion can fail when the text has no valid representation.
try:
    int("twenty")
except ValueError as error:
    print(type(error).__name__)  # Expected output: ValueError

# bool follows truthiness: empty containers and zero are false; non-empty values are true.