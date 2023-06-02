"""
    Write a Python program that accepts a sequence of comma-separated numbers
    from the user and generates a list and a tuple of those numbers.
"""

inputString = input("Enter values seperated by commas")
generatedList = inputString.split(",")
generatedTuple = tuple(generatedList);
print(generatedList)
print(generatedTuple)