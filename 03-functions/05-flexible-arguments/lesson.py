"""Lesson: *args collects positional values and **kwargs collects named values."""

def total(*numbers):
    return sum(numbers)


def describe(**details):
    for key, value in details.items():
        print(key, value)


print(total(2, 4, 6))
describe(name="Ada", role="programmer")