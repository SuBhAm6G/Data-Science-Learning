# # Write a function that removes leading and trailing whitespace and also replaces all internal sequences of whitespace with a single space.
def space_remover(s):
    lst=list(s.strip().split())
    return " ".join(lst)
s="   hello   world   python   "
print(space_remover(s))

# Write a function that trims custom characters from the left and right but must preserve them if they appear in the middle.
def trim_custom(s,c):
    start=end=0
    start=next((i for i,ch in enumerate(s) if ch!=c), 0)
    end=next((i for i,ch in enumerate(reversed(s)) if ch!=c), 0)
    #next return only first item on a iterator, it stops after getting a value
    end=len(s)-end    

    return s[start:end]

print(trim_custom("***abc**", "*"))