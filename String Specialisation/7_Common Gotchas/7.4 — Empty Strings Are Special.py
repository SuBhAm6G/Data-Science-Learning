s = "   "
if s.strip():
    print("Input accepted")

data = ["hello", "", "   ", "\n", "world"]
count=0
for s in data: 
    if s.strip():
        count+=1
print(count)
