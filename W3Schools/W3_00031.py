"""
    Write a Python program that computes the greatest common divisor (GCD) of
    two positive integers where num1 > num2
"""

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
gcd = 1

for num in range(1, int(num2/2) + 1):
    if num1 % num == 0 and num2 % num == 0:
        gcd = num

print(gcd)
