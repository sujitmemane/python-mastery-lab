"""Solutions for list practice."""

foods = ["rice", "apples", "soup"]
print(foods)

drinks = ["water", "soda", "juice"]
drinks.append("tea")
drinks.remove("soda")
print(drinks)

for position, drink in enumerate(drinks):
    print(position, drink)

numbers = [8, 3, 12, 5]
largest = numbers[0]
for number in numbers[1:]:
    if number > largest:
        largest = number
print(largest)