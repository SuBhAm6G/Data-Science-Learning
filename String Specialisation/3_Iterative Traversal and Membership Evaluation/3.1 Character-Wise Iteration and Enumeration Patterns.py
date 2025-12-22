#enumeration
s="Hello?Woerld"
for i,ch in enumerate(s):
    if(ch=='?'): print(f"? found at index: {i}")

# Write a function that takes a string and returns a new string where every digit is replaced with *.
def asterisk(s):
    s2=""
    for ch in s:
        s2+='*' if ch.isdigit() else ch
    return s2
s="a1b2c3"
print(asterisk(s))

# Using only iteration (no built-in find, index, or replace), write a function that returns the index of the second occurrence of a given character in a string.
# Return -1 if there is no second occurrence.
def second_occurence(s,c):
    count=0
    for i,ch in enumerate(s):
        if ch==c:
            count+=1
            if count==2:
                return i
    return -1

s="hello"
print(second_occurence(s,'l'))