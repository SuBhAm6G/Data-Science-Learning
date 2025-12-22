# Technique A — partition / rpartition (first / last split)
# Use when you want the piece before/after the first (or last) separator and don't want to build many parts.
s="subham@gmail.com"
local,sep,domain=s.partition("@")
print(local)
print(sep)
print(domain)

# Technique B — find + slicing for "between markers"
# You often need the substring between start_marker and end_marker:
s="username_4017#"
def between(s,a,b):
    i=s.find(a)
    if i==-1:
        return ""
    i+=len(a)
    j=s.find(b,i)
    if j==-1:
        return ""
    return s[i:j]
print(between(s,'_','#'))

# Technique C — split(sep, maxsplit=n) when you only need limited fields
# To efficiently get the first few tokens:
s = "a,b,c,d,e"
first_two = s.split(",", 2)  
print(first_two)

# Technique D — Extract Nth field without full split (streaming find)
# If the input is huge and you only want the k-th field, loop with find advancing the start index:
def nth_field(s, sep, n):   # n is 0-based
    start=0
    for _ in range(n):
        idx=s.find(sep,start)
        if(idx==-1):
            return ""
        start=idx+len(sep)
    idx=s.find(sep,start)
    if idx==-1:
        return s[start:]
    return s[start:idx]

s = "field1,field2,field3,field4"
print(nth_field(s, ",", 2))  # Output: field3

# Technique E — Use rfind or rpartition for suffix extraction (file extension, last path part)
path = "/home/me/docs/report.pdf"
head, sep, tail = path.rpartition("/")  # head = "/home/me/docs", tail = "report.pdf"
name, sep, ext = tail.rpartition(".")   # ext = "pdf"

# Technique F — startswith / endswith for boundary checks
# Before extracting, sometimes check shape cheaply:
s="people.txt"
if s.endswith(".txt"):
    base = s[:-4]
print(base)

######
def ext(s):
    head, sep, tail = s.rpartition(".") #takes the last appearance of sep in rfind
    if sep == "":
        return ""
    return tail
print(ext("bol.yt.gz"))

#Problem 1
# Write a function between(s, a, b) that returns the substring between the first occurrence of a and the first occurrence of b that comes after a.
# Return an empty string if the markers are not found in that order. Use find() and slicing; do not use regular expressions.
def between(s,a,b):
    i=s.find(a,0)
    if (i==-1):
        return ""
    i+=len(a)
    j=s.find(b,i)
    if(j==-1):
        return ""
    return s[i:j]
print(between("<<hello>>","<<",">>"))

#Problem 2
# Write nth_field(s, sep, n) which returns the n-th field (0-based) from s split by separator sep, without using split() (i.e., do not create the full list). If the field doesn't exist return "". Your implementation should be efficient for large strings and separators of length > 1.
def nth_field(s, sep, n):   # n is 0-based
    start=0
    for _ in range(n):
        idx=s.find(sep,start)
        if(idx==-1):
            return ""
        start=idx+len(sep)
    idx=s.find(sep,start)
    if idx==-1:
        return s[start:]
    return s[start:idx]

s = "field1,field2,field3,field4"
print(nth_field(s, ",", 2))