"""Lesson: change loop behavior with break, continue, and pass."""

for number in range(1, 6):
    if number == 4:
        break
    print(number)

print("---")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# break stops the loop completely. continue skips to the next iteration.

for item in ["ready", "later"]:
    if item == "later":
        pass  # A placeholder that intentionally does nothing.
    print(item)
