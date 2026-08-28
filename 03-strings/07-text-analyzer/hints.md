# Hints

1. Build normalized text with a loop and `character.isalnum()`.
2. Call `.split()` after replacing punctuation with spaces.
3. Loop through `text.lower()` and test membership in `"aeiou"`.
4. Use a dictionary for the report and a frequency dictionary for the common word.

Check empty input before indexing the most-common result. Keep original and normalized text in separate variables.