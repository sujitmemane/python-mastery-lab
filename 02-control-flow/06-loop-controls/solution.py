"""Solutions for loop-control practice."""


def stop_at_seven():
    for number in range(1, 11):
        print(number)
        if number == 7:
            break


def print_odds():
    for number in range(1, 11):
        if number % 2 == 0:
            continue
        print(number)


def first_multiple_of_fifteen():
    for number in range(1, 31):
        if number % 3 == 0 and number % 5 == 0:
            return number
    return None


def print_nonempty_names(names):
    for name in names:
        if name == "":
            continue
        print(name)


if __name__ == "__main__":
    stop_at_seven()
    print_odds()
    print(first_multiple_of_fifteen())
    print_nonempty_names(["Asha", "", "Ravi", "", "Mina"])
