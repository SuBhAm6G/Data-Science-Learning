from pathlib import Path
import re
# Write a function make_safe_path(base_dir, filename) that:
# Uses pathlib
# Sanitizes filename
# Returns a safe absolute path inside base_dir
def make_safe_path(base_dir, filename):
    safe_name = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)

    base = Path(base_dir).resolve()
    path = (base / safe_name).resolve()

    if not str(path).startswith(str(base)):
        raise ValueError("Unsafe path detected")

    return path

# Problem:
# Write a function write_safe(base_dir, filename, text) that:
# Prevents path traversal
# Creates directory if missing
# Writes UTF-8 text safely
# Never overwrites an existing file
# (Hint: use exists())
def write_safe(base_dir, filename, text):
    safe_path = make_safe_path(base_dir, filename)

    # Ensure the directory exists
    safe_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if the file already exists
    if safe_path.exists():
        raise FileExistsError(f"The file '{safe_path}' already exists and will not be overwritten.")

    # Write the text to the file in UTF-8 encoding
    with open(safe_path, 'w', encoding='utf-8') as f:
        f.write(text)