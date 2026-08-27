"""Practice: write decisions with if."""

# Level 1 — Print "positive" if number is greater than zero.
number = 8
if number>0:
    print("positive")

# Level 2 — Print "adult" if age is at least 18.
age = 21
if age>18:
    print("adult")



# Level 3 — Print "can borrow" only when the user has a library card
# and has no overdue books.
has_library_card = True
has_overdue_books = False
if has_overdue_books and has_library_card:
    print("can borrow")


# Level 4 — Debug this code: identify the error, then fix it.
score = 75
if score >= 50:
    print("pass")