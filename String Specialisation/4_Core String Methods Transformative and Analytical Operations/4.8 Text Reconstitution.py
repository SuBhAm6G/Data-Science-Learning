def normalize_spaces(s):
    return " ".join(word for word in s.strip().split())
s="  hello   \t world \n python  "
print(normalize_spaces(s))