import re
# Extract all email addresses from a string and return them as a list.
s="Mail me at a@x.com or support@site.org"
emails=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',s)
print(emails)

# Clean a string so that:

# extra spaces are collapsed
# punctuation is removed
# text is lowercased
s="Hello!!!   This is   CLEANING."
cleaned=re.sub(r'[^\w\s]|\s+', ' ', s.lower()).strip()

print(cleaned)