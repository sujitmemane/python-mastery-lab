"""Solutions for function-values practice."""

def apply_once(function, value):
    return function(value)


def triple(number):
    return number * 3


words = ["alpha", "echo", "bravo", "delta"]
scores = [55, 72, 91, 64, 88]

def transform(values, function):
    return [function(value) for value in values]


print(apply_once(triple, 4))
print(sorted(words, key=lambda word: word[-1]))
print(list(filter(lambda score: score >= 70, scores)))
print(transform([0, 10, 20], lambda celsius: celsius * 9 / 5 + 32))