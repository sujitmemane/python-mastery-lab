# 03 - Strings

Strings are immutable sequences of text. This section moves from reading characters to building reliable text transformations.

## Lesson Plan

| Order | Topic | Difficulty | Practice goal |
| --- | --- | --- | --- |
| 1 | Creating and indexing | Beginner | Read individual characters safely |
| 2 | Slicing and stepping | Beginner | Extract, skip, and reverse text |
| 3 | Cleaning, case, and replacement methods | Beginner+ | Normalize and manipulate text |
| 4 | Formatting with f-strings | Beginner+ | Build readable, precise output |
| 5 | Immutability and transformations | Intermediate | Create changed text without changing the source |
| 6 | Searching, testing, splitting, and joining | Intermediate | Find structure and move between text and words |
| 7 | Text analyzer capstone | Intermediate+ | Combine methods, loops, and collections |

## How To Study

For every lesson, read the objective and mental model in `lesson.py`, predict the output, run it, and then solve `practice.py` without opening the solution. Use hints one at a time. Write down what each method returns and answer the active-recall question in your own words.

### Method Map

- Clean and change case with `strip`, `lstrip`, `rstrip`, `lower`, `upper`, `title`, `capitalize`, and `swapcase`.
- Replace content with `replace`, `removeprefix`, and `removesuffix`.
- Search with `in`, `find`, `index`, `count`, `startswith`, and `endswith`.
- Validate character content with `isalpha`, `isdigit`, `isalnum`, and `isspace`.
- Convert between text and pieces with `split`, `rsplit`, `splitlines`, and `join`.

Methods return new strings or other values. They do not mutate the original string. Prefer a named transformation pipeline over one unreadable chain, and remember that `index()` raises an exception when `find()` returns `-1` for a missing substring.

### Real-World Connections

These operations appear in command-line input cleanup, CSV-like parsing, log processing, search, validation, report generation, and API payload preparation. A robust text pipeline usually normalizes first, then parses, counts, and formats at the boundary.

## Capstone: Text Analyzer

Build a reusable analyzer for a paragraph. Report original character count, non-space character count, word count, vowel count, unique-word count, the most common word, and a list of words longer than six characters. Treat capitalization and punctuation consistently, handle empty input, and preserve the original text. Explain where each string method is used and test at least one repeated word.

Start with [01 - indexing](01-indexing/lesson.py).