"""
    Write a Python program to get n (non-negative integer) copies of the first 2 characters
    of a given string. Return n copies of the whole string if the length is less than 2.
"""

ipStr = input("Enter string")
lengthOfString = len(ipStr)
n = int(input("Enter n"))

if lengthOfString < 2:
    print(n*ipStr)
else:
    print(n*ipStr[0:2])