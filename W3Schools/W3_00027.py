"""
    Write a Python program that concatenates all elements in a list into a string and returns it.
"""

list = [1, 2, 3, 4, 5, 12, 3, 41]
concatString = ""
for listItem in list:
    concatString = concatString + str(listItem)

print(concatString)