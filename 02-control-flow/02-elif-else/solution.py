"""Solutions for the elif and else practice."""


def size_label(number):
    if number < 10:
        return "small"
    elif number < 100:
        return "medium"
    else:
        return "large"


def temperature_label(temperature):
    if temperature < 15:
        return "cold"
    elif temperature < 30:
        return "warm"
    else:
        return "hot"


def score_label(score):
    if score < 0 or score > 100:
        return "invalid"
    elif score >= 50:
        return "pass"
    else:
        return "fail"


if __name__ == "__main__":
    print(size_label(50))
    print(temperature_label(24))
    print(score_label(75))