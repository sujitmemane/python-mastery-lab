"""Practice: implement each TODO without opening solution.py."""

# Level 1 — Bind your name to a variable and print it.
name="Sujit"
print(name)


# Level 2 — Swap the values of left and right using Python unpacking.
left = "L"
right = "R"

left,right=right,left
print(left,right)


# Level 3 — Unpack this tuple into city and country, then print both.
location = ("Bengaluru", "India")
(K,C) = location
print(K,C)


# Level 4 — Predict before running: what will numbers contain after this?
numbers = [1, 2]
alias = numbers
alias.append(3)
print(numbers)
# TODO: add 3 through alias, then print numbers and explain the result.