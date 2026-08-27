"""Solutions for the if practice."""


def describe_number(number):
    if number > 0:
        return "positive"
    return "not positive"


def describe_age(age):
    if age >= 18:
        return "adult"
    return "not adult"


def can_borrow(has_library_card, has_overdue_books):
    if has_library_card and not has_overdue_books:
        return "can borrow"
    return "cannot borrow"


if __name__ == "__main__":
    print(describe_number(8))
    print(describe_age(21))
    print(can_borrow(True, False))