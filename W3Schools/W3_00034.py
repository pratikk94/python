"""
    Write a Python program that returns true if the two given integer
    values are equal or their sum or difference is 5.
"""


def custFunction(num1, num2):
    if num1 + num2 == 5 or abs(num1 - num2) == 5:
        return True
    else:
        return False


print(custFunction(3, 8))
print(custFunction(-1, 4))
print(custFunction(100, 2))
