a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b) # 4 integer division, rounded down towards minus infinity. Important if an integer MUST be used.
print(a % b)  # 0 modulo: the remainder integer division

print()


# For the variable i, look for the integers in rage of 1 through a divided by b.
# If you use "/" instead of "//" you'll get an error because "/" will only look for floating point when line 17
# Is specifically for looking for integers, thus you MUST use "//"
for i in range(1, a // b):
    print(i)
