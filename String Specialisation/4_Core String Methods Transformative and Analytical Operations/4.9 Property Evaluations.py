# Write a function:

# def count_types(s):

# Return a dictionary with counts of:
# alphabetic characters
# digits
# whitespace
# others
def count_types(s):
    property={"alpha","digits","whitespace","others"}
    dic={x: 0 for x in property}
    for ch in s:
        if ch.isalpha(): dic["alpha"]+=1
        elif ch.isdigit(): dic["digits"]+=1
        elif ch.isspace(): dic["whitespace"]+=1
        else: dic["others"]+=1
    return dic
s="hello world 123 !@#"
print(count_types(s))


def extract_numbers(s):
    num_lst=[]
    current=""
    for ch in s:
        if ch.isnumeric(): current+=ch
        else:
            if current:
                num_lst.append(current)
                current=""
    if current:
        num_lst.append(current)
    return num_lst

s="vals:٢٣,45;Ⅷ" 
print(extract_numbers(s))