"""Lesson: a text analyzer composes small string operations into a pipeline.

Objective: normalize text, tokenize it, and calculate useful measurements.
Mental model: raw text enters a pipeline; each stage produces data for the
next stage. Keep the original input available for the original count.
"""

from collections import Counter

text = "Code well. Code often!"
normalized = "".join(character.lower() if character.isalnum() else " " for character in text)
words = normalized.split()
counts = Counter(words)

print(f"Characters: {len(text)}")
print(f"Words: {len(words)}")
print(f"Unique words: {len(set(words))}")
print(f"Most common: {counts.most_common(1)[0]}")

# Active recall: why should punctuation be normalized before counting words?