"""
    Write a Python program to retrieve the path and name of the file currently being executed.
"""

import os
print("Current File Name : ",os.path.realpath(__file__))