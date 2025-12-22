# You are given:

b = b"na\xefve"

# Decode using Latin-1
# Re-encode to UTF-8
# Print the final UTF-8 bytes
decoded_latin=b.decode("latin-1")
print(decoded_latin)
re_encoded_utf=decoded_latin.encode("utf-8")
print(re_encoded_utf)


# You are given mixed-encoding byte strings:

data = [
    b"caf\xe9",        # Latin-1 encoded café
    b"hello",          # ASCII
    b"\xe2\x82\xac100" # UTF-8 encoded €100
]
# Task:
# Decode each string correctly
# Convert all text to lowercase
# Extract digits only
# Concatenate them into one integer

decoded_data = []
for item in data:
    try:
        decoded_data.append(item.decode("utf-8"))
    except UnicodeDecodeError:
        decoded_data.append(item.decode("latin-1"))

import re
number_pattern = re.compile(r'\d+')
final_digits = ""
for text in decoded_data:
    lower_text = text.lower()
    matches = number_pattern.findall(lower_text)
    final_digits += "".join(matches)

if final_digits:
    print(int(final_digits))
else:
    print(0)