# Write a function nth_index(s, sub, n) that returns the index of the n-th occurrence (1-based) of sub in s.
def nth_index(s, sub, n):
    start=0
    for _ in range(n):
        idx=s.find(sub,start)
        if(idx==-1): return -1
        else: start=idx+len(sub)
    return start-len(sub)

# print(nth_index("hello world hello", "hello", 1))  # 0
# print(nth_index("hello world hello", "hello", 2))  # 12
# print(nth_index("hello world hello", "hello", 3))  # -1
# print(nth_index("banana", "na", 1))
# print(nth_index("banana", "na", 2))
# print(nth_index("banana", "na", 3))

# Write a function split_once_from_right(s, sep) that behaves like splitting by sep but only at the last occurrence, returning a tuple (head, sep, tail).
def split_once_from_right(s, sep):
    split_idx=s.rfind(sep)
    if split_idx==-1:
        return ("","",s)
    return (s[0:split_idx],sep, s[split_idx+len(sep):])
print(split_once_from_right("a/b/c", "/"))
print(split_once_from_right("hello", "/"))
print(split_once_from_right("foo--bar--baz", "--"))

