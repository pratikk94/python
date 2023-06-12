"""
    Write a Python program to compute the future value of a specified principal amount,
    rate of interest, and number of years.
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
"""

PA = int(input("Principal amount ->"))
R = float(input("Rate of interest ->"))
N = int(input("Number of years ->"))

futureValue = PA*((1 + R/100)**N)
print(futureValue)
