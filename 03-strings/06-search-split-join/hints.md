# Hints

1. Use `.startswith("admin")`.
2. Use `.find(":")`; the result is an integer index.
3. Use `.split(",")` and loop through the returned list.
4. Use `.split()` with no argument, then `"-".join(words)`.

`find()` returns `-1` when absent; `index()` raises an exception, so choose based on whether absence is expected.