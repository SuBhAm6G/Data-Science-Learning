def valid_username(s):
    if not (3 <= len(s) <= 15):
        return False
    return all(ch.islower() or ch.isdigit() or ch == "_" for ch in s)

# Once it finds one character where all three conditions are False, it stops immediately and returns False.

def valid_identifier(s):
    return (
        s.isidentifier() and not s[0].isdigit()
    )

# print(valid_identifier('56Subh'))
# print(valid_identifier('Xe3'))

# Write a function is_valid_username(s) that:
# Assumes input is already standardized
# Length is between 5 and 12
# Contains only lowercase letters and digits
# Must start with a letter
def is_valid_username(s):
    if not (5<=len(s)<=12):
        return False
    if not ('a'<=s[0]<='z'):
        return False
    return all('0'<=ch<='9' or 'a'<=ch<='z' for ch in s)
# print(is_valid_username("al!"))

# Problem:
# Write a function validate_integer(s) that:
# Accepts optional leading + or -
# Rejects empty strings
# Rejects numbers with leading zeros (except "0")
# Contains digits only otherwise

def validate_integer(s):
    if not s:
        return False
    if s[0] in '+-':
        if (len(s))>1:
            if (s[1]=='0'): return False
            else: s=s[1:]
        else:
            return False
    if not s.isdigit():
        return False
    if len(s)>1 and s[0]=='0':
        return False
    return True
    
print(validate_integer("+-"))