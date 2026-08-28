"""Lesson: dictionaries map unique keys to values."""

scores = {"Ava": 91, "Ben": 84}
scores["Mia"] = 96
scores["Ava"] += 2
print(scores["Ava"])

for name, score in scores.items():
    print(name, score)