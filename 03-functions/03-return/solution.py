"""Solutions for return practice."""

def square(number):
    return number * number


def larger(first, second):
    if first > second:
        return first
    return second


def is_even(number):
    return number % 2 == 0


numbers = [2, 7, 10, 13, 18]
even_count = 0
for number in numbers:
    if is_even(number):
        even_count += 1
print(square(5), larger(3, 8), even_count)