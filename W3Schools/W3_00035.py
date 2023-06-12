"""
    Write a Python program to add two objects if both objects are integers.
"""

obj1 = 1
obj2 = 2
if type(obj1) is int and isinstance(obj2,int):
    print(obj1+obj2)
else:
    print("Types not int")