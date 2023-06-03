"""
    Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
num = int(input("enter number"))
if 900 <= num < 1100:
    print(str(num) + " is in 100 between 1000")
elif 1900 <= num < 2100:
    print(str(num) + " is in 100 between 2000")
else:
    print("Not matching criteria")