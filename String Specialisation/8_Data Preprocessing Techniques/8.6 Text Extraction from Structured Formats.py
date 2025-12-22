# Write a function parse_line(line) that:
# Parses a comma-separated line
# Strips whitespace
# Converts empty fields to None
def parse_line(line):
    return [f.strip() if f.strip() else None for f in line.split(',')]

# Write a function parse_records(lines) that:
# Takes a list of CSV-like lines
# Ignores empty lines
# Parses quoted fields correctly
# Returns list of parsed rows
def parse_records(lines):
    records = []
    for line in lines:
        if not line or not line.strip():
            continue
        fields = []
        current = []
        inside_quotes = False
        for ch in line:
            if ch == '"':
                inside_quotes = not inside_quotes
            elif ch == ',' and not inside_quotes:
                fields.append("".join(current).strip())
                current = []
            else:
                current.append(ch)
        fields.append("".join(current).strip())
        records.append(fields)
    return records