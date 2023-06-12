"""
    Write a Python program to sum two given integers. However, if the sum is
    between 15 and 20 it will return 20.
"""

num1 = int(input("num 1 ->"))
num2 = int(input("num 2 ->"))

if 15<num1+num2<20:
    print(20)
else:
    print(num1+num2)

