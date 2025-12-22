import re
# Write a function that returns the first word starting with a capital letter in a sentence.
def capital(s):
    match=re.search(r'\b[A-Z][a-zA-Z]*\b',s)
    return match.group() if match else None
s="today is Sunny and Warm"
print(capital(s))

# Extract all overlapping occurrences of the substring "ana" in a string using regex tools.
def extract_ana(s):
    return [(m.start(),m.group(1)) for m in re.finditer(r'(?=(ana))',s)]
s="banana anagram analysis"
print(extract_ana(s))