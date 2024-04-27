"""
Use a context manager to read files.
You can recognise a context manager
by the 'with' statement.

with open() as name:
   d = json.load(file_handle)  # reads into a dictionary

open() opens a file.
mode='r' means read.
encoding='utf-8' is what you usually want to use!

"""
import json

# use json.load() to read the whole file into a dictionary
# use
with open(file="example.json", mode="r", encoding="utf-8") as json_file:
    example_dict = json.load(json_file)  # safe inside the with

print(example_dict)
print(f"{example_dict['a key']=}")
print(f"{example_dict['names'][0]=}")
print(f"{example_dict['shape']['colour']=}")
# It's just a python dictionary now,
# Can access keys and values just
# like any other dictionary.
# THIS DOESN'T CHANGE THE FILE CONTENTS!
for key in example_dict.keys():
    print(f"{key=}")
print()

for value in example_dict.values():
    print(f"{value=}")
print()

for key, value in example_dict.items():
    print(f"{key=} has {value=}")
print()

# Add to the dictionary
example_dict['numbers'] = [1, 2, 3, 4]
print(example_dict)
print(f"{example_dict['numbers']=}")
print()

# Add to a list in the dictionary
example_dict['names'].append('Bethan')
print(example_dict)
print(f"{example_dict['names'][-1]=}")

for key in ('names', 'numbers', 'cars'):
    if key in example_dict:  # in looks at the keys
        print(f'{key} is in the dictionary')
    else:
        print(f'{key} is *not* in the dictionary')

assert 'numbers' in example_dict
assert 'Bethan' in example_dict['names']


# Read the file again:
print('\nReading the file again...')
with open(file="example.json", mode="r", encoding="utf-8") as json_file:
    read_again = json.load(json_file)  # safe inside the with

# The things we added aren't in the file
assert 'numbers' not in read_again
assert 'Bethan' not in read_again['names']

