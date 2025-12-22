import re
# Write a regex that finds all repeated consecutive words in a string.
s="yes yes no no maybe"
results=re.findall(r'\b(\w+)\s+\1\b',s)
print(results)

# Write a regex that extracts all words that contain a repeated letter, like:
s="The cool breeze fluttered by"
words = [m.group(0) for m in re.finditer(r'\b\w*([A-Za-z])\1\w*\b', s, flags=re.I)]#Use re.I (case-insensitive)
print(words)