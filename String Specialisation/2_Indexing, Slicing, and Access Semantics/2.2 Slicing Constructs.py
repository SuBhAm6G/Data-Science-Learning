# Intermediate Question

# Write a function that returns every third character of a string starting from index 0.
s="ABCDEFGHIJK"
print(s[::3])

# Hard Question

# Given a string, return a new string consisting of:

# characters from index 1 to -1 (exclusive)

# but taken in reverse order

# and only every second character

# You must use slicing.

# Example:
# Input: "PYTHONIC"
# Process: middle part "YTHONI" → reverse → "INOHTY" → take every 2nd → "IOH"

s="PYTHONIC"
s1=s[1:-1]
s2=s1[::-1]
print(s2[::2])