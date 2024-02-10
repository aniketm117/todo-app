import random

a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

if a < b:
    c = random.randint(a, b)
    print(c)
else:
    print("Re-enter the values of lower and upper bound")