import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    #Status code of 1 usually means something went wrong.
    sys.exit(1)

print(f"{x} / {y} = {result}")