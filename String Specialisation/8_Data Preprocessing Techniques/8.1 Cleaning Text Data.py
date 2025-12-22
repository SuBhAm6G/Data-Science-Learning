# Problem:
# Write a function clean_text(s) that:
# Removes leading & trailing whitespace
# Removes all null characters
# Collapses multiple spaces into a single space
# Example:

Input="  hi\x00\x00   there   "
def clean_text(s):
    s=s.replace("\x00", "")
    return " ".join(s.split())
print(clean_text(Input))  
print(len(clean_text(Input)))

# Write a function sanitize(s) that:
# Removes control characters (ASCII < 32)
# Preserves newlines (\n)
# Collapses multiple spaces
# Removes leading/trailing whitespace from each line
def sanitize(s):
    filtered="".join(ch for ch in s if ch>=' ' or ch in '\n')
    lines=filtered.split('\n')
    filtered_lines=[]
    for line in lines:
        cleaned=" ".join(line.split())
        filtered_lines.append(cleaned)
    return '\n'.join(filtered_lines)



s="  hi\x00\n\n  there\t\t  "
print(sanitize(s))
print(len(sanitize(s)))