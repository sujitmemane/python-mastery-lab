"""Solutions for flexible argument practice."""

def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def announce(*names):
    for name in names:
        print(f"Hello, {name}!")


def settings(**options):
    for option, value in options.items():
        print(option, value)


print(product(2, 3, 4))
announce("Ava", "Mia")
settings(theme="light", notifications=True)