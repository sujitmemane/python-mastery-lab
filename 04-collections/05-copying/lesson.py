"""Lesson: assignment aliases a list; copy creates a separate outer list."""

original = ["draft"]
alias = original
alias.append("published")
print(original)

clone = original.copy()
clone.append("archived")
print(original)
print(clone)