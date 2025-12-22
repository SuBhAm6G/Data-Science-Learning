# Write a function standardize_word(s) that:
# Removes leading/trailing whitespace
# Collapses internal whitespace
# Converts to lowercase (Unicode-safe)
# Example:
def standardize_word(s):
    return " ".join(s.casefold().strip().split())
Input="  PyThOn   LanGuAge "
print(standardize_word(Input))

# Write a function canonical_text(s) that:
# Applies Unicode-safe case normalization
# Standardizes whitespace per line
# Preserves empty lines
# Ensures consistent comparison across inputs

def canonical_text(s):
    lines=s.splitlines()
    return '\n'.join(" ".join(line.casefold().split()) for line in lines)
s="  HELLO   World\n\n  PyThOn\tRocks "
print(canonical_text(s))