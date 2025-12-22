# You are given a UTF-8 encoded byte string:

b = b"Python\xe2\x9c\x85"
decoded=b.decode().upper()
print(decoded)
encoded=decoded.encode("utf-8")
print(encoded)

# You receive mixed input:

# Task:
# Decode each element safely using UTF-8
# Extract only numeric characters
# Concatenate them into one integer
# Output the final integer
import re
data = [b"123", b"456\x72", b"78\xe2\x82\xac", b"90"]
number=re.compile(r'\d+')
decoded=[element.decode("utf-8") for element in data]
print(decoded)
final_str=""
for element in decoded:
    num=number.search(element)
    if num:final_str+=num.group(0)
print(int(final_str))