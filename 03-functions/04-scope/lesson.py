"""Lesson: local names exist inside their function; global names are outside."""

message = "outside"

def show_message():
    message = "inside"
    print(message)


show_message()
print(message)