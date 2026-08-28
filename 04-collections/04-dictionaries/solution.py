"""Solutions for dictionary practice."""

movie = {"title": "Arrival", "year": 2016}
movie["rating"] = 8.0
print(movie.get("director", "Unknown"))

inventory = {"pens": 12, "notebooks": 4, "erasers": 9}
for item, quantity in inventory.items():
    print(item, quantity)

words = ["red", "blue", "red", "green", "blue", "red"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)