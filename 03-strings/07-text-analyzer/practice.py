"""Capstone: build a reusable text analyzer."""

# Implement separate functions for these responsibilities:
# 1. normalize(text): lowercase letters, replace punctuation with spaces.
# 2. words_from(text): return normalized words.
# 3. count_vowels(text): count a, e, i, o, and u without counting y.
# 4. analyze(text): return a dictionary with character_count,
#    non_space_count, word_count, vowel_count, unique_word_count,
#    most_common_word, and long_words (length > 6).
# Challenge: return None for most_common_word when text has no words, preserve
# the original text for character_count, and test repeated words.