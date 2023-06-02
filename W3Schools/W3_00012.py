"""    Write a Python program that prints the calendar for a given month and year.
    Note : Use 'calendar' module
"""
import calendar

y = int(input("enter year"))
m = int(input("enter month"))

print(calendar.month(y,m))