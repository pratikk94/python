"""
    Write a Python program to create a histogram from a given list of integers.
"""
ipList = input("Enter list").split(",")
for ipListItem in ipList:
    for count in range(0, int(ipListItem)):
        print("@", end='')
    print(" ")
