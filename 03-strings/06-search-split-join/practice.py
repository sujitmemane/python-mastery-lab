"""Practice: search and reshape text."""

# Level 1 - Check whether a username starts with "admin".
username = "admin_reader"
print(username.startswith("admin"))

# Level 2 - Find the position of the colon in this record.
record = "status:ready"
print(record.find(":"))

# Level 3 - Split this CSV-like line and print each field.
line = "Ava,42,active"
arr  = line.split(",")
for a in arr:
    print(a)

# Level 4 - Clean repeated spaces, then join the words with hyphens.
title = "  Python   String   Tools  "
title_arr = "-".join(title.split())
print(title_arr)

# Challenge: explain when `find()` is safer than `index()`.