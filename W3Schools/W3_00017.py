"""
    Write a Python program to calculate the difference between a given number and 17.
    If the number is greater than 17, return twice the absolute difference.
"""

no = int(input("Enter number"))
if no >= 17:
    print(2*abs(no-17))
else:
    print(17-no)