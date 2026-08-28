"""Lesson: methods clean and transform strings by returning new values.

Objective: normalize user-facing text and choose the right method family.
Mental model: a method is a small tool attached to the string value.
"""

message = "  Hello, Python learner!  "
cleaned = message.strip()
print(cleaned)
print(cleaned.lower())
print(cleaned.upper())
print(cleaned.title())
print(cleaned.replace("learner", "developer"))
print("report.csv".removesuffix(".csv"))
print("user:123".removeprefix("user:"))

# Active recall: why does message still contain its spaces after these calls?
