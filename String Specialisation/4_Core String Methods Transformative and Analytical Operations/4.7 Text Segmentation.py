# Write a function:

# def split_first_word(s):

# It should return a tuple: (first_word, rest_of_string)
def split_first_word(s):
    return tuple(s.split(" ",1))
s="Hello World here I'm"
print(split_first_word(s))  


# Write a function:

# def parse_path(path):

# Rules:
# Path components are separated by /
# Ignore empty components (e.g. "//home///user" → ["home","user"])
# The function must return a list of cleaned components
def parse_path(path):
    lst=path.split("/")
    filtered_lst=list(filter(None, lst))
    return filtered_lst
path="//home///user/docs/"
print(parse_path(path))
