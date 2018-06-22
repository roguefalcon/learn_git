#!/usr/bin/python3

from datetime import date

# Print the date header
print("===============================")
print("|  Date Printer, 2018         |")
print("===============================")

today = str(date.today())
print("Today's date is", today)


# We want to print the Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, etc.
def F():
    a, b = 0, 1
    while a <= 100:
        yield a
        a, b = b, a + b


def print_fibonacci():
    for cur in F():
        print(str(cur) + ',', end='')


print_fibonacci()
print('')  # Print the newline
