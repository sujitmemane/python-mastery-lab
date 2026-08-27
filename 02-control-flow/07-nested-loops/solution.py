"""Solutions for nested-loop practice."""


def rectangle():
    for row in range(3):
        for column in range(4):
            print("*", end=" ")
        print()


def triangle():
    for row in range(1, 4):
        for column in range(row):
            print("*", end=" ")
        print()


def small_multiplication_table():
    for first in range(1, 4):
        for second in range(1, 4):
            print(f"{first} x {second} = {first * second}")


def count_matching_pairs(values):
    matching_pairs = 0
    for first_index in range(len(values)):
        for second_index in range(first_index + 1, len(values)):
            if values[first_index] == values[second_index]:
                matching_pairs += 1
    return matching_pairs


if __name__ == "__main__":
    rectangle()
    triangle()
    small_multiplication_table()
    print(count_matching_pairs([1, 2, 1, 3]))
