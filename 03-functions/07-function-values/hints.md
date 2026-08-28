# Hints

1. Pass `triple`, not `triple()`, to `apply_once`.
2. A key function can be `lambda word: word[-1]`.
3. The condition is `lambda score: score >= 70`.
4. Call `function(value)` for each value and collect the results.

Think: a lambda is useful for a tiny one-off rule; use a named function when the rule needs a name or explanation.