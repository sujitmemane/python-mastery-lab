"""Solutions for decorator practice."""

def double(number):
    return number * 2


def validate_non_negative(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result >= 0:
            print("valid")
        return result
    return wrapper


@validate_non_negative
def subtract(first, second):
    return first - second


print(double(4))
print(subtract(5, 2))
print(subtract(2, 5))