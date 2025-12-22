def space_remover(s):
    lst=list(s.strip().split())
    return " ".join(lst)
s="   hello   world   python   "
print(space_remover(s))