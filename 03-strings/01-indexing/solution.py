"""Solutions for string indexing practice."""

word = "developer"
print(word[0])
print(word[-1])

word = "python"
print(word[len(word) // 2])

word = "coding"
for index in range(len(word)):
    print(index, word[index])

word = "banana"
first_character = word[0]
count = 0
for character in word:
    if character == first_character:
        count += 1
print(count)
