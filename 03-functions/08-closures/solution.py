"""Solutions for closure practice."""

def make_prefix(prefix):
    def add_prefix(message):
        return prefix + message
    return add_prefix


add_warning = make_prefix("Warning: ")
print(add_warning("low disk space"))

def make_counter():
    count = 0

    def next_count():
        nonlocal count
        count += 1
        return count

    return next_count


counter = make_counter()
print(counter(), counter())