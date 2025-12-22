# Write a function that returns the three central characters of any odd-length string using indexing (not slicing).
# Example:
# "PYTHONIC" → "HON"
s="PYTHONIC"
mid=int(len(s)/2)
central=s[mid-1]+s[mid]+s[mid+1]
print(central)

# You are given a string.
# Using only indexing (no slicing allowed), construct and return a new string containing:

# the first character

# the last character

# the second character

# the second-to-last character

# In that order.

# Example:
# "ABCDE" → "AEBD"
s="ABCDE"
new_s=s[0]+s[-1]+s[1]+s[-2]
print(new_s)