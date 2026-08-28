"""Solutions for text-processing practice."""

text = "Hello World"
lower_text = text.lower()
print(text)
print(lower_text)

text = "Python makes sense"
vowel_count = 0
for character in text.lower():
    if character in "aeiou":
        vowel_count += 1
print(vowel_count)

sentence = "read code write code repeat"
print(len(sentence.split()))

text = "Python is clear and powerful"
vowel_count = 0
for character in text.lower():
    if character in "aeiou":
        vowel_count += 1
print(f"Characters: {len(text)}")
print(f"Words: {len(text.split())}")
print(f"Vowels: {vowel_count}")
