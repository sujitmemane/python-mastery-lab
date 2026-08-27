"""Solutions for data type practice."""


def type_names(values):
    return [type(value).__name__ for value in values]


def integer_checks(value):
    return isinstance(value, int), isinstance(value, str)


if __name__ == "__main__":
    print(type_names([42, 3.14, 1 + 2j, "hello", False, None]))
    print(integer_checks(10))