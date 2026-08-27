"""Practice: process each item with a for loop."""

# Level 1 — Print every item in this list on its own line.
colors = ["red", "green", "blue"]
for color in colors:
    print(color)


# Level 2 — Print the length of every word.
words = ["python", "code", "loop"]
for word in words:
    print(len(word))


# Level 3 — Calculate the total of all numbers without using sum().
numbers = [4, 7, 2, 9]
sum=0
for number in numbers:
    sum+=number
print(sum)


# Level 4 — Count how many vowels appear in this word.
text = "programming"
count=0
vowel = "aeiou"
for t in text:
    if t in vowel:
        count+=1
print(count)