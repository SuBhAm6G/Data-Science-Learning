# You are given a very long string s.

# Task:
# Remove all digits
# Convert remaining characters to lowercase
# Do this efficiently (no O(n²) behavior)
s="Th1s 1s A L0ng Str1ng W1th D1g1ts 1234567890"
s_lst=[]
for ch in s:
    if ch.isalpha() or ch.isspace():
        s_lst.append(ch.lower())
print("".join(s_lst))