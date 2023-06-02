"""

Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java

"""

inputFileName = input("Enter file name")
fileList = inputFileName.split(".")
print(fileList[-1])