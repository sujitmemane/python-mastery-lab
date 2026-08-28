"""Practice: format values with f-strings."""

# Level 1 - Print a sentence using name and city.
name = "Asha"
city = "Pune"
print(f"My name is {name} and I am from {city}")


# Level 2 - Print the total price with two decimal places.
price = 12.5
quantity = 3
print(f"The total price is {price*quantity:.2f}")


# Level 3 - Print a score as a percentage with one decimal place.
score = 0.934
print(f"{score:.1%}")




# Level 4 - Create a simple receipt line using item, quantity, and total.
item = "Notebook"
quantity = 2
unit_price = 4.75
print(f"I purchased {quantity} {item} each cost me {unit_price} that makes total {unit_price * quantity:.2f}")
