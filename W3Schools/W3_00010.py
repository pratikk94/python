"""
    Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
    Sample value of n is 5
    Expected Result : 615
"""

sampleValue = "5"
count = int(sampleValue)
sampleValue = sampleValue + "5"
count = count + int(sampleValue)
sampleValue = sampleValue + "5"
count = count + int(sampleValue)

print(count)
