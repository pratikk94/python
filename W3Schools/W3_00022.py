"""
    Write a Python program to count the number 4 in a given list.
"""

userList = [4, 1, 2, 3, 5, 2, 4, 4]
count = 0
for item in userList:
    if item == 4:
        count = count + 1

print(count)