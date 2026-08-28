"""Solutions for string-method practice."""

text = "  Python Is Fun  "
print(text.strip().lower())

message = "This is a bad example. A bad habit can change."
print(message.replace("bad", "good"))

filename = "ID:notes.txt"
print(filename.removeprefix("ID:").removesuffix(".txt"))

label = "   PRIORITY    TASK   "
words = label.strip().lower().split()
print(" ".join(words))
