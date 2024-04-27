"""


"""

import json

A_PYTHON_DICTIONARY = {
    "a key": "a value",
    "names": ["Chloe", "Raju"],
    "polygon": {"colour": "Red",
                "sides":  10}
}

# use write() to write the whole multi line strin as a file
with open(file="write_json_file_example_1.txt", mode="w", encoding="utf-8") as target_json_file:
    # target_json_file is out file handle (TextIOWrapper)
    # Can't use write for a dictionary. You'd get
    # a TypeError: write() argument must be str, not dict

    string = json.dumps(A_PYTHON_DICTIONARY)
    target_json_file.write(string)


# use json.dumps to make a nicely formatted string
# us write to write the ehole string to a file
with open(file="write_json_file_example_2.txt", mode="w", encoding="utf-8") as target_json_file:
    # target_json_file is out file handle (TextIOWrapper)
    string_from_json_dumps = json.dumps(A_PYTHON_DICTIONARY, indent=2)
    target_json_file.write(string_from_json_dumps)


# THIS IS THE CORRECT WAY TO DO IT IN ONE LINE !
# use.json.dump to convert the dictionary into a
# nicely formatted string and write it for us.
with open(file="write_json_file_example_3.txt", mode="w", encoding="utf-8") as target_json_file:
    # target_json_file is out file handle (TextIOWrapper)
    json.dump(obj=A_PYTHON_DICTIONARY, fp=target_json_file, indent=4)


# Set a debug point here, to be able to see the files.


# Tidy up (delete) the files we just wrote
from pathlib import Path
for filename in ("write_json_file_example_1.txt", "write_json_file_example_2.txt", "write_json_file_example_3.txt"):
    path = Path(filename)
    input(f"Examine the file at {path}, then press returnb to erase it")
    path.unlink()  # deletes the file


