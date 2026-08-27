"""Solutions for conversion practice."""


def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    print(int("19") + 1)
    print(float("3.50") * 2)
    print(safe_int("not a number"))