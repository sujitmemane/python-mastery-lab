"""Solutions for search, split, and join practice."""

username = "admin_reader"
print(username.startswith("admin"))

record = "status:ready"
print(record.find(":"))

line = "Ava,42,active"
for field in line.split(","):
    print(field)

title = "  Python   String   Tools  "
print("-".join(title.split()))