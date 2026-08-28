"""Practice: clean and transform text with string methods."""

# Level 1 - Strip the spaces and print this text in lowercase.
text = "  Python Is Fun  "
cleaned=text.strip()
print(cleaned)


# Level 2 - Replace every "bad" with "good" and print the result.
message = "This is a bad example. A bad habit can change."
print(message.replace("bad","good"))

# Level 3 - Remove the "ID:" prefix and the ".txt" suffix.
filename = "ID:notes.txt"
print(filename.removeprefix("ID:").removesuffix(".txt"))

# Level 4 - Normalize this label to lowercase with single spaces between words.
# Challenge: use a pipeline that remains readable rather than one giant line.
label = "   PRIORITY    TASK   "
print(label.strip().lower().join(label.split()))
