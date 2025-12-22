import re
# Write a function that:
# Replaces all multiple spaces (2 or more) with exactly one space
def space_normaliser(s):
    clean=re.sub(r"\s+"," ", s).strip()
    return clean
s="Python   is   great" 
print(space_normaliser(s))

# Write a function using re.split that:
# Splits a string into words, separating by ANY punctuation (.,!?;:), but keeps the words only.
def word_splitter(s):
    words=re.split(r"[.,!?;:\s]", s)
    return list(filter(None,words))
s="Hello, world! This is great: isn't it?"
print(word_splitter(s))