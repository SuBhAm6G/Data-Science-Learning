# Given a string s and integer k:
# Task:
# Remove the k-th character (1-based index)
# Return the new string
# Must handle edge cases safely
def func(s,k):
    if k>len(s): return s
    return s[:k-1]+s[k:]
s="abcdef"
print(func(s,4))
