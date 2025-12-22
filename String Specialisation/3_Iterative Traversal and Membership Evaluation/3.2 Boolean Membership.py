# Write a function that checks whether a string contains any digits using only in (no loops, no isdigit).
def digit_check(s):
    warn=set("01234567890")
    for ch in s:
        if ch in warn:
            return True
    return False

s="Hello123"
print(digit_check(s))  # True
s="hello"
print(digit_check(s))  # False

# Write a function that returns True only if all characters in s are from a given allowed set, using only in and iteration.
def all_allowed(s, allowed):
    for ch in s:
        if ch not in allowed:
            return False
    return True
s="abcde"
allowed="abcde"
print(all_allowed(s,allowed)) # True
s="abcfg"
print(all_allowed(s,allowed)) # False
