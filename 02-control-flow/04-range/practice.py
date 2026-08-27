"""Practice: use range() to repeat a known number of times."""

# Level 1 — Print numbers from 0 through 9.
for i in range(0,10):
    print(i)


# Level 3 — Print all even numbers from 2 through 20.
for i in range(0,21):
    if i%2==0:
        print(i)

# Level 4 — Calculate 5! (5 * 4 * 3 * 2 * 1) using a loop and range().
sum=1
for i in range(1,6):
    sum*=i
print(sum)