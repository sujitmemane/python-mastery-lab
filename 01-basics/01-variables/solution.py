"""Solutions for the variables practice."""


def swap_values(left, right):
    """Return the values in reversed order using tuple unpacking."""
    right, left = left, right
    return left, right


def unpack_location(location):
    """Return a location tuple as separate city and country values."""
    city, country = location
    return city, country


def demonstrate_aliasing():
    """Show that two names can refer to the same mutable list."""
    numbers = [1, 2]
    alias = numbers
    alias.append(3)
    return numbers, alias


if __name__ == "__main__":
    print(swap_values("L", "R"))
    print(unpack_location(("Bengaluru", "India")))
    print(demonstrate_aliasing())