s='subham'
b=s.encode("utf-8")
print(b)

text="café"
with open("a.txt",'r+',encoding="utf-8") as f:
    f.write(text)

s1 = "hello\nworld"
s2 = "hello\\nworld"
print(s1,s2)