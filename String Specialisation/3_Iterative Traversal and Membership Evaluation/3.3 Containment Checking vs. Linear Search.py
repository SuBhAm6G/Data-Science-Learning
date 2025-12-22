password = "hello@123"
forbidden = "@#$"
if any (ch in forbidden for ch in password):
    print("Password contains forbidden characters")

# Write a function that returns True if a string contains any lowercase letters, using the most efficient method possible.
def LC(s):
    for ch in s:
        if 'a'<=ch<='z':
            return True
    return False
s="ABC123"
print(LC(s))  
s="aBC123"
print(LC(s))

# Write a function that checks whether every vowel in a string appears at least once.
# Use a linear search pattern, NOT helpful built-ins like count or find.
def vowelcheck(s):
    vowels=set("aeiou")
    for item in vowels:
        if item in s: continue
        else: return False
    return True

s="aeioubcdf"
print(vowelcheck(s))  # True
s="aeibcdf"
print(vowelcheck(s))  # False