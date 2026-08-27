"""Practice: select between multiple outcomes."""

# Level 1 — Print "small", "medium", or "large" for a number.
number = 50
if number<10:
    print("small")
elif number <50:
    print("medium")
else:
    print("large")

# Level 2 — Classify temperature as cold (<15), warm (<30), or hot.
temperature = 24
if temperature < 15:
    print("cold")
elif temperature <30:
    print("warm")
else:
    print("hot")


# Level 3 — Create a function that returns "invalid" for negative scores,
# "pass" for scores from 50 to 100, and "invalid" for scores above 100.

def create_result(mark):
    if mark<0 or mark>100:
        return "Invalid Integer"
    elif mark>=50:
        return "Pass"
    else:
        return "Fail"


print(create_result(-4))