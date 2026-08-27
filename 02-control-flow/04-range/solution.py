"""Solutions for range practice."""


def numbers_zero_to_nine():
    return list(range(10))


def numbers_one_to_ten():
    return list(range(1, 11))


def even_numbers_to_twenty():
    return list(range(2, 21, 2))


def factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    print(numbers_zero_to_nine())
    print(numbers_one_to_ten())
    print(even_numbers_to_twenty())
    print(factorial(5))