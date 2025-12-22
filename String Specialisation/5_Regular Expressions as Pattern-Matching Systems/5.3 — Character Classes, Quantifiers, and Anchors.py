import re
# Write a regex that extracts all 4-letter words from a string.
s="In many ways, code is life"
results=re.findall(r'\b\w{4}\b',s)
print(results)

# Write a regex that extracts all words containing at least two consecutive vowels.
s="beautiful cooperation queue boot"
results=re.findall(r'\b\w*[aeiouAEIOU]{2}\w*\b',s)
print(results)