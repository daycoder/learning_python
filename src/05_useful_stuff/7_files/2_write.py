"""


"""

from pathlib import Path

TEXT_TO_WRITE_TO_FILE = """(Writing) Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

path = Path("write_file_example.txt")

# use write() to write the whole multi-line TEXT_TO_WRITE_TO_FILE string to a file
with open(file=path, mode="w", encoding="utf-8") as file_to_wrtie_to:
    file_to_wrtie_to.write(TEXT_TO_WRITE_TO_FILE)

input(f"Examine the file at {path}, then press returnb to erase it >")

# erase the file
path.unlink()
