"""Practice: convert input-like values safely."""

# Level 1 — Convert "19" to an integer and add 1.
string = "19"
print(int(string)+1)


# Level 2 — Convert "3.50" to a float and multiply it by 2.
my_height="3.50"
print(float(my_height)*2)


# Level 3 — Write a function that returns None instead of crashing for invalid integers.
try:
    int("sixty-nine")
except ValueError as error:
    print("None")