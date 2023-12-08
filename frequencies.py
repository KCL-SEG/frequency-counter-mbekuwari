"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:

        value = str(item)
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    # Your code goes here
    return frequencies
