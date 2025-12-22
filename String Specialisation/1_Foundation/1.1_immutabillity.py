s = "hello"
print(id(s))
s = s + " world"
print(id(s))  # Different ID → new object created

#Use-case A: Understanding why string concatenation in loops is slow
result=""
for i in range(5):
    result+=str(i) #O(n2)

#solution
parts=[]
for i in range(5):
    parts.append(str(i))
result="".join(parts)

# Use-case B: Why slicing is fast
# Although slicing creates a new string, Python knows exactly how many characters to copy, making it very efficient.
s = "hello world"
piece = s[6:]

# Use-case C: Safely sharing strings
# Multiple variables can reference the same string since it cannot be mutated.
a='python'
# Assign 'python' to 'a'
b=a
# 'b' now references the same string object as 'a'
# No risk: modifying a cannot change b because modification creates a new string.

#Problems
# What is the output of the following?

s = "cat"
t = s
s += "s"
print(s, t)

def reverse_good(s):
    return s[::-1]
print(reverse_good('aku'))