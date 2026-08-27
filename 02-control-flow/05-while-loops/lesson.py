"""Lesson: repeat a block while a condition remains true."""

count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1

# Expected output:
# Count: 1
# Count: 2
# Count: 3
#
# A while loop needs a condition and a state change. Without count += 1,
# the condition would stay true forever.

password = "python"
attempt = ""
while attempt != password:
    attempt = password

print("Access granted")
