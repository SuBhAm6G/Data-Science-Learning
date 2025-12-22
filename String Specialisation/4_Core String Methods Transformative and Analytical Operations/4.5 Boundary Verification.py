# Write a function that checks whether a given filename is a valid Python file.
# Valid extensions: .py, .pyw.
def validity_check(s):
    return s.endswith((".py",".pyw"))
print(validity_check("my_program.py"))
print(validity_check("my_program.pyw"))
print(validity_check("my_program.txt"))

# Write a function that returns True if a URL begins with "http://" or "https://",
# and ends with one of the following domain extensions:
# .com
# .org
# .net
# .io
def valid_check(s):
    return s.startswith(("http://","https://")) and s.endswith((".com",".org",".net",".io"))
print(valid_check("http://www.example.com"))   # True
print(valid_check("https://www.example.org"))  # True
print(valid_check("ftp://www.example.net"))    # False
print(valid_check("http://www.example.co"))    # False
