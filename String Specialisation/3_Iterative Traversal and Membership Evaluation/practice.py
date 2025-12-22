# Write a function that returns a new string where all non-ASCII characters are replaced with "?".
def replace(s):
    s=s.encode("ascii",errors="replace")
    return s.decode("utf-8")
s="café naïve"
print(replace(s))  # "cafe? na?ve"

# Write a function that returns the reversed substring between the first and last digit in a string.
def func(s):
    start=-1
    end=-1
    for i,ch in enumerate(s):
        if ch.isdigit(): 
            start=i+1
            break
    for j in range(len(s)-1, -1, -1):
        if s[j].isdigit(): 
            end=j
            break
    if start==-1 or end==-1:
        return ""
    return s[start:end][::-1]

s="a1bc2d3e"
print(func(s))  # "d2cb"

# Write a function that removes repeated consecutive characters from a string.
def remover(s):
    result=[s[0]]
    for ch in s[1:]:
        if result[-1]!=ch:
            result.append(ch)
        else:
            continue
    return result
s="aaabbbccdaa"
print(''.join(remover(s)))  # "abcda"