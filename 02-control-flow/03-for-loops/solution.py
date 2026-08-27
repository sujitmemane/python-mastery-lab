"""Solutions for the for-loop practice."""


def print_items(items):
    for item in items:
        print(item)


def word_lengths(words):
    return [len(word) for word in words]


def manual_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


if __name__ == "__main__":
    print_items(["red", "green", "blue"])
    print(word_lengths(["python", "code", "loop"]))
    print(manual_total([4, 7, 2, 9]))
    print(count_vowels("programming"))