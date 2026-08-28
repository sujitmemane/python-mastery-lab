"""Solutions for scope practice."""

score = 10

def show_score():
    local_score = 20
    print(local_score)
    return local_score


show_score()
print(score)

def display_score(value):
    print(value)


display_score(score)