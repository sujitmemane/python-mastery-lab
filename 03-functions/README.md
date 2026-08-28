# 03 - Functions

Functions name a job, accept inputs, and may produce an output. They are the main unit for making Python programs readable, testable, and reusable.

## Lesson Plan

| Order | Concept | Difficulty | Practice goal |
| --- | --- | --- | --- |
| 1 | Defining and calling functions | Beginner | Package repeated instructions |
| 2 | Parameters and arguments | Beginner+ | Make behavior configurable |
| 3 | Return values and `print()` | Beginner+ | Produce values other code can use |
| 4 | Scope and function design | Intermediate | Control names and side effects |
| 5 | `*args`, `**kwargs`, and argument rules | Intermediate | Accept and forward flexible arguments |
| 6 | Decomposition and function design | Intermediate | Split a problem into small testable functions |
| 7 | Functions as values | Intermediate | Pass behavior into another function |
| 8 | Nested functions and closures | Intermediate+ | Preserve state safely |
| 9 | Decorators | Advanced | Add logging or validation around a function |
| 10 | Decomposition capstone | Advanced | Build a small reusable reporting program |

## How To Study

For every lesson, read the objective and mental model in `lesson.py`, predict and run its output, then complete `practice.py` without opening the solution. Use one hint at a time. In your own words, answer the active-recall question before checking the solution.

### Design Questions

- Does this function have one clear responsibility?
- Should it return data, print a message, or do both? Prefer returning data in reusable code.
- Which inputs should be required, and which should have defaults?
- Does it mutate anything or perform I/O? Make side effects visible at the boundary.

### Real-World Connections

The same boundaries appear in API handlers, validation helpers, service functions, file parsers, and tests. `*args` and `**kwargs` are useful for forwarding options, while decorators commonly provide logging, authentication, caching, and timing.

## Capstone: Report Builder

Build a command-line-style report from a list of transaction dictionaries. Create separate functions to validate a record, calculate totals, filter by category, format a line, and assemble the report. Return values between functions instead of relying on global state. Include invalid-record handling, at least one higher-order helper, and assertions for normal and edge cases.

Start with [01 - defining and calling](01-defining/lesson.py).