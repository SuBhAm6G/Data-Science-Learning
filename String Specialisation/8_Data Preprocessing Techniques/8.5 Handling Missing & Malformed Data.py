# Write a function safe_string(s, default="UNKNOWN") that:
# Returns default if s is missing
# Otherwise returns cleaned & standardized text
# (Missing includes: None, empty, whitespace-only, "na", "null")
def safe_string(s, default="UNKNOWN"):
    if s is None:
        return default
    s=s.strip()
    if not s:
        return default
    if s.strip().casefold() in {'na','null','none'}:
        return default
    return s.casefold()
s="   pnull"
print(safe_string(s))

# Write a function parse_int_field(s, default=None) that:
# Returns default if s is missing
# Returns an integer if valid
# Raises ValueError if malformed
def parse_int_field(s, default=None):
    if s is None:
        return default
    s=s.strip()
    if not s:
        return default
    if s.strip().casefold() in {'na','null','none'}:
        return default
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Malformed integer: {s}")

print(parse_int_field('   566d '))