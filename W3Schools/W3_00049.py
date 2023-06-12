"""
    Write a Python program to list all files in a directory.
"""

from os import listdir
from os.path import isfile, join
path = "/Users/pratik/PycharmProjects/pythonProject/W3Schools"
files_list = [f for f in listdir(path) if isfile(join(path, f))]
print(files_list);