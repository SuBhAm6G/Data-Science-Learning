# Write a function read_clean_lines(path) that:
# Reads a UTF-8 text file
# Removes leading/trailing whitespace
# Skips empty lines
# Returns a list of strings
def read_clean_lines(path):
    with open(path,'r',encoding="utf-8") as f:
        lines=[line.strip() for line in f if line.strip()]
    return lines

# Write a function normalize_file(input_path, output_path) that:
# Reads a UTF-8 text file
# Normalizes each line (Unicode NFC, casefold, whitespace)
# Writes normalized text to a new file
# Preserves line order
def normalize_file(input_path, output_path):
    import unicodedata
    with open(input_path,'r',encoding="utf-8") as fin,\
        open(output_path,'w',encoding="utf-8") as fout:

        for line in fin:
            line=line.rstrip('\n')
            normalized=unicodedata.normalize("NFC",line)
            normalized=normalized.casefold()
            normalized=" ".join(normalized.split())
            fout.write(normalized+'\n')
            