"""Practice: control when a loop continues or stops."""

# Level 1 - Print numbers from 1 upward, stopping when you reach 7.
for number in range(1, 11):
    if number == 7:
        break
    print(number)
 


# Level 2 - Print only odd numbers from 1 through 10 using continue.
for number in range(1, 11):
    if number % 2 == 0:
       continue
    print(number)


# Level 3 - Search for the first number divisible by both 3 and 5.
for number in range(1, 31):
    if number % 3 == 0 and number % 5 ==0:
        print(number)
        break
    


# Level 4 - Ignore empty strings and print the remaining names.
names = ["Asha", "", "Ravi", "", "Mina"]
for name in names:
    if name=="":
        continue
    print(name)
