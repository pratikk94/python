"""
    Write a Python program to calculate the sum of three given numbers.
    If the values are equal, return three times their sum
"""

inputStr = input("Enter 3 numbers")
numList = inputStr.split(",")

if int(numList[0]) == int(numList[1]) and int(numList[1]) == int(numList[2]):
    sum = 3 * int(numList[0])
    print("All equal")
else:
    sum = int(numList[0]) + int(numList[1]) + int(numList[2])

print(sum)
