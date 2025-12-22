# Write a function that takes a list of strings and returns a new list where all strings are converted to lowercase except strings that already contain digits (leave those unchanged).
def func(lst):
    new_lst=[]
    for s in lst:
        if any(ch.isdigit() for ch in s): new_lst.append(s)
        else: new_lst.append(s.lower())
    return new_lst
lst=["Hello", "WORLD", "aAbc123", "PYTHON"]
print(func(lst))  

# Implement a case-insensitive string comparison function without using lower() or upper(), but you may use casefold().
def equal_ignore_case(a, b):
    return a.casefold()==b.casefold()
print(equal_ignore_case("Hello", "hello"))  # True
print(equal_ignore_case("Pytho1n", "PYTHON"))  # False
