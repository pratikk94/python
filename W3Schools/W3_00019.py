"""
    Write a Python program to get a newly-generated string from a given string where
    "Is" has been added to the front. Return the string unchanged if the given string
    already begins with "Is".
"""

ipString = input("Enter a string")

if ipString[0] != "I" and ipString[1] !="s":
    ipString = "Is "+ ipString;

print(ipString)