#Q1
# Write a function:

# def reverse_middle(s):

# It should:
# Leave the first 2 characters and last 2 characters unchanged.
# Reverse everything in between using slicing.
# If the string length < 5, return the original string unchanged.
def reverse_middle(s):
    reversed_mid_s=s[2:-2][::-1]
    new_s=s[:2]+reversed_mid_s+s[-2:]
    return new_s
s="Porcupine"
print(reverse_middle(s))  # Output: 

#Q2
# Write a function:

# def extract_deep(s):

# Rules:
# Find the first "("
# Then find the first ")" after that index
# Extract what’s inside
# Now inside that extracted substring,
# find "[" and the next "]"
# return ONLY what’s inside the brackets
# If anything is missing, return ""

def extract_deep(s,a,b):
    i=s.find(a,0)
    if i==-1: return ""
    i+=len(a)
    j=s.find(b,i)
    if j==-1: return ""
    return s[i:j]

s="abc(def[ghi]xyz)123"
s2=extract_deep(s,'(',')')
print(f"Inside parentheses: {s2}")
s3=extract_deep(s2,'[',']')
print(f"Inside brackets: {s3}")


#Q3
# Write a function:

# def split_into_pairs(s):

# It must:
# Break a string into chunks of exactly 2 characters
# You must use slicing, no loops allowed except maybe a range step
# If the string has odd length, the last chunk contains just the last character
def split_into_pairs(s):
    return [s[i:i+2] for i in range(0,len(s),2)]
s="ABCDEFG"
result=split_into_pairs(s)
print(result)