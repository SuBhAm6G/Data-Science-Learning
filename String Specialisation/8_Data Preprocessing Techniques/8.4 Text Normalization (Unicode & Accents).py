import unicodedata

# Write a function normalize_name(s) that:
# Applies Unicode NFC normalization
# Removes accents
# Converts to lowercase (Unicode-safe)
# Collapses whitespace
def normalize_name(s):
    s=unicodedata.normalize('NFC',s)
    s=unicodedata.normalize('NFD',s)
    accent_removed_s=("".join(ch for ch in s if not unicodedata.combining(ch))).casefold()
    return " ".join(word for word in accent_removed_s.split())
print(normalize_name("  JOSÉ   Silva "))

# Write a function canonical_key(s) that:
# Produces a comparison-safe key
# Treats accented and unaccented letters as equal
# Is case-insensitive
# Preserves internal spaces but normalizes them
# Is safe for dictionary/set keys
def canonical_key(s):
    s=unicodedata.normalize('NFD',s)
    accent_removed_s=("".join(ch for ch in s if not unicodedata.combining(ch))).casefold()
    return " ".join(word for word in accent_removed_s.split())
print(canonical_key("CAFÉ MOCHA"))