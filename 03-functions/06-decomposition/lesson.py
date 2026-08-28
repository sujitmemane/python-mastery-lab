"""Lesson: small functions make a process easier to read and test."""

def clean_words(text):
    return text.lower().split()


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


text = "Code well code often"
print(count_words(clean_words(text)))