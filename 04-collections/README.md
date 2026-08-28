# 04 - Collections

Collections hold related values. Choosing the right one affects readability, mutation, lookup speed, and what operations naturally express the problem.

## Lesson Plan

| Order | Concept | Difficulty | Practice goal |
| --- | --- | --- | --- |
| 1 | Lists: create, index, and slice | Beginner | Read ordered data safely |
| 2 | Lists: update, iterate, and nest | Beginner+ | Transform sequences and records |
| 3 | Tuples and unpacking | Beginner+ | Represent fixed-position data |
| 4 | Sets and set operations | Intermediate | Model unique membership and overlap |
| 5 | Dictionaries and iteration | Intermediate | Model key-value data |
| 6 | Nested data and membership | Intermediate | Process JSON-like records |
| 7 | Mutability, references, and copying | Intermediate+ | Predict and control shared state |
| 8 | List, set, and dictionary comprehensions | Intermediate+ | Write concise transformations |
| 9 | Choosing a collection and capstone | Advanced | Select structures based on trade-offs |

## How To Study

For every lesson, read the objective and mental model in `lesson.py`, predict and run its output, then complete `practice.py` without opening the solution. Use one hint at a time. Explain the active-recall question in your own words.

### Choosing A Collection

Use a list for an ordered, changeable sequence; a tuple for a fixed record or unpackable return value; a set for unique membership and set algebra; and a dictionary for key-based lookup. These are guidelines, not laws: consider ordering, mutation, duplicates, hashability, and how readers will use the data. A set is not a replacement for a list when order or duplicate occurrences matter.

### Real-World Connections

Lists commonly hold records, tuples represent coordinates or rows, sets remove duplicate permissions or tags, and dictionaries model configuration and API-like data. Nested combinations such as a list of dictionaries are normal in data-processing code.

## Capstone: Order Analyzer

Process a dataset of customer orders without being told which collection to use. Report unique customers, totals by product, products bought by two customers, and the highest-value order. Use loops first, then improve at least one transformation with a comprehension. Explain each collection choice and include an empty-data case.

The numbered folders combine the two closely related topics in the final row: [07 - nested data](07-nested-data/lesson.py) and [08 - choosing a collection](08-choosing-capstone/lesson.py) follow the six foundational lessons.

Start with [01 - lists](01-lists/lesson.py).