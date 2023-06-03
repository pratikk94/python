"""
    Write a Python program to test whether a passed letter is a vowel or not.
"""
c = input("enter character")
if c.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")