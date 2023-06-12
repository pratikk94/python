"""
    Write a Python program to sum three given integers. However, if two values are equal,
    the sum will be zero.
"""

num1 = int(input("Num 1"))
num2 = int(input("Num 2"))
num3 = int(input("Num 3"))

if num1 == num2 or num2 == num3 or num1 == num3:
    print(0)
else:
    print(num1+num2+num3)