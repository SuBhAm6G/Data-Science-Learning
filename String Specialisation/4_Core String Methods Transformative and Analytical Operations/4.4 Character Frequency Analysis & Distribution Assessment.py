# Write a function that returns a dictionary mapping each vowel (a, e, i, o, u) to the number of times it appears in a string.
def func(s):
    vowels=['a','e','i','o','u']
    freq={x:0 for x in vowels}
    for ch in s:
        if ch in vowels:
            freq[ch]=freq.get(ch,0)+1
    return freq
s="hello world"
print(func(s))

# Write a function that analyzes a string and returns the character(s) with the highest frequency.
def counter(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    max_value=max(freq.values())
    result=[ch for ch,v in freq.items() if v==max_value]
    return result

s="aaachybfgbb"
print(counter(s))  
