"""
    Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

x1, y1 = input("Enter point 1").split(",")
x2, y2 = input("Enter point 2").split(",")

print(((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5)
