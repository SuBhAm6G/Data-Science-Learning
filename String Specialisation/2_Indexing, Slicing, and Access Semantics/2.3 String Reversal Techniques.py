s = "PYTHON"
rev_s="".join(reversed(s))
print(rev_s)

# Reverse everything except the first and last characters.

s = "ABCDEFG"
s2=s[1:-1][::-1]
s3=s[0]+s2+s[-1]
print(s3)

# Use Case 3 — Reverse words individually in a sentence
sentence = "hello world python"
rev_sentence=" ".join(word[::-1] for word in sentence.split())
print(rev_sentence)

# Write a function that:

# takes a string

# reverses only characters at even indices, keeping odd-indexed characters unchanged

# Example:
# Input: "PYTHON"
# Even indices: P T O → reversed: O T P
# Output should place them back into even positions → "OYTPHN"
def custom_rev(s):
    even=list(s[0::2][::-1])
    lst=list(s)
    j=0
    for i in range(len(lst)):
        if(i%2==0):
            lst[i]=even[j]
            j+=1
    new_s="".join(lst)
    return new_s
print(custom_rev("PYTHON"))

# You are given a string.
# Construct a new string that is:

# The reverse of the original

# But every 3rd character (starting from the reversed string’s index 0) should be uppercase

# All other characters should become lowercase

# Example:
# Input: "ABCDEFGHIJK"
# Reversed → "KJIHGFEDCBA"
# Apply rule → "KjiHgfEdcBa"
s="ABCDEFGHIJK"
rev_s=list(s[::-1].lower())
for i in range(len(rev_s)):
    if i%3==0:
        rev_s[i]=rev_s[i].upper()
new_s="".join(rev_s)
print(new_s)