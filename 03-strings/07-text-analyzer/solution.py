"""Reference solution for the text-analyzer capstone."""

from collections import Counter


def normalize(text):
    characters = []
    for character in text.lower():
        characters.append(character if character.isalnum() else " ")
    return "".join(characters)


def words_from(text):
    return normalize(text).split()


def count_vowels(text):
    return sum(character in "aeiou" for character in text.lower())


def analyze(text):
    words = words_from(text)
    frequencies = Counter(words)
    return {
        "character_count": len(text),
        "non_space_count": sum(not character.isspace() for character in text),
        "word_count": len(words),
        "vowel_count": count_vowels(text),
        "unique_word_count": len(set(words)),
        "most_common_word": frequencies.most_common(1)[0][0] if words else None,
        "long_words": sorted({word for word in words if len(word) > 6}),
    }


report = analyze("Code well. Code often!")
print(report)
assert report["most_common_word"] == "code"
assert analyze("")["most_common_word"] is None