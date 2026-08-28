"""Solutions for parameter practice."""

def double(number):
    return number * 2


def repeat(message, times):
    for _ in range(times):
        print(message)


def format_name(first, last, title="Student"):
    return f"{title}: {first} {last}"


print(double(6))
repeat("Keep going", 2)
print(format_name(last="Lovelace", first="Ada"))