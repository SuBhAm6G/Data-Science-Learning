s = "abc"
if s.find("a")!=-1:
    print("Found a")

# You are given a string s:
# Task:
# Extract substring after the first :
# If : does not exist, return the original string
# Must not crash
def func(s):
    pos=s.find(':')
    if pos==-1:
        return s
    return s[pos+1:]
s1="key:value"
s2="novaluehere"
print(func(s1))
print(func(s2))