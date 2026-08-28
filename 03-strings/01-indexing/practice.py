"""Practice: access characters by index."""

# Level 1 - Print the first and last character.
word = "developer"
print(word[0],word[-1])


# Level 2 - Print the middle character of this odd-length word.
word = "python"
middle_term = len(word)//2 
print(word[middle_term])


# Level 3 - Print each character with its index.
word = "coding"
for i in range(0,len(word)):
    print(word[i],f"{i}")


# Level 4 - Count how many times the first character appears.
word = "banana"
count=0
for l in word:
    if l=="b":
        count+=1

print(count,"Count")
