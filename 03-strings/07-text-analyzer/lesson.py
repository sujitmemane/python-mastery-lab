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
# Result: Characters: 22
print(f"Words: {len(words)}")
# Result: Words: 4
print(f"Unique words: {len(set(words))}")
# Result: Unique words: 3
print(f"Most common: {counts.most_common(1)[0]}")
# Result: Most common: ('code', 2)

# Why normalize first? Without replacing punctuation, "often!" and "often"
# would be counted as different words. Keep text and normalized separate so the
# original character count remains available.

# Common mistake:
# counts.most_common(1)[0] fails for empty input. Check whether words exist
# before indexing the first result.

# Active recall: why should punctuation be normalized before counting words?