"""Solutions for operator practice."""


def divide_with_remainder(number, divisor):
    return number // divisor, number % divisor


def is_in_range(number):
    return 10 <= number <= 20


def contains_admin(username):
    return "admin" in username


if __name__ == "__main__":
    print(divide_with_remainder(17, 5))
    print(is_in_range(15))
    first = [1, 2]
    second = [1, 2]
    print(first == second, first is second)
    print(contains_admin("admin_user"))