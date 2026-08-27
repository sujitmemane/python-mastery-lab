"""Solutions for while-loop practice."""


def print_one_to_five():
    number = 1
    while number <= 5:
        print(number)
        number += 1


def countdown():
    number = 5
    while number >= 1:
        print(number)
        number -= 1
    print("Blast off!")


def sum_one_to_ten():
    value = 1
    total = 0
    while value <= 10:
        total += value
        value += 1
    return total


def double_until_hundred(number):
    while number < 100:
        number *= 2
    return number


if __name__ == "__main__":
    print_one_to_five()
    countdown()
    print(sum_one_to_ten())
    print(double_until_hundred(3))
