"""Lesson: methods clean and transform strings by returning new values.

Objective: normalize user-facing text and choose the right method family.
Mental model: a method is a small tool attached to the string value.
"""

message = "  Hello, Python learner!  "
cleaned = message.strip()
print(cleaned)
# Result: Hello, Python learner!
print(cleaned.lower())
# Result: hello, python learner!
print(cleaned.upper())
# Result: HELLO, PYTHON LEARNER!
print(cleaned.title())
# Result: Hello, Python Learner!
print(cleaned.replace("learner", "developer"))
# Result: Hello, Python developer!
print("report.csv".removesuffix(".csv"))
# Result: report
print("user:123".removeprefix("user:"))
# Result: 123

# Useful tests return booleans rather than changed text:
print("123".isdigit(), "Python".isalpha(), " ".isspace())
# Result: True True True

# Common mistake:
# Calling cleaned.lower() does not update cleaned. Assign the result when the
# transformed value is needed later.

# Active recall: why does message still contain its spaces after these calls?
