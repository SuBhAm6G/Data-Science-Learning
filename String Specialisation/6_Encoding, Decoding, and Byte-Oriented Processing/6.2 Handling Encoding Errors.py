# You are given:
b = b"hello\xffworld"
# Decode using UTF-8
# Replace invalid bytes
# Print the result
decoded=b.decode("utf-8",errors="replace")
print(decoded)

# You receive a list of unknown-encoding byte strings:

data = [
    b"100\xe2\x82\xac",
    b"200\xff",
    b"30\n"
]

# Task:
# Decode each using UTF-8 without crashing
# Extract only digits
# Sum all extracted numbers
# Output the final sum as an integer
decoded_data=[x.decode("utf-8", errors="ignore") for x in data]
import re
number=re.compile(r'\d+')
total=0
for data in decoded_data:
    num=number.search(data)
    if num: total+=int(num.group(0))

print(total)