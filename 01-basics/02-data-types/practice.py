"""Practice: identify and use Python's basic types."""

# Level 1 — Create one value of each: int, float, complex, str, bool, and None.
age = 45
gold_value = 16,578
crazy_value= 5+6j
name="sujit"
is_adult=True
is_gay=None



# Level 2 — Print the type name of each value in this list.
values = [42, 3.14, 1 + 2j, "hello", False, None]
for value in values: 
    print(type (value))


# Level 3 — Use isinstance to check whether 10 is an int and a str.
print(isinstance(10,int))