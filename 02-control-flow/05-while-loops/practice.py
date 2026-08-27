"""Practice: repeat work with while loops."""

# Level 1 - Print numbers from 1 through 5.
number = 1
while number <= 5:
    print(number)
    number+=1


# Level 2 - Count down from 5 to 1, then print "Blast off!".
countdown = 5
while countdown >= 1:
    print(countdown)
    countdown-=1


# Level 3 - Calculate the sum of numbers from 1 through 10.
value = 1
total = 0
while value <= 10:
    total+=value
    value+=1


# Level 4 - Double a number until it is at least 100.
value = 3
while value < 100:
    value = value*2
print(value)
