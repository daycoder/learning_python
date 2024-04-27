"""
An ValueError is raised for a few reasons.
e.g.
     * the value doesn't exist
     * the value can't be converted
"""

some_letters = ['a', 'b', 'c']
print(f'{len(some_letters)=}')
for letter in some_letters:
    print(f"for {letter=}, {some_letters.index(letter)=}")

try:
    # Getting the index of a value in
    # a list that doesn't exist
    some_letters.index('d')
except ValueError as ve:  # <-- catch the IndexError
    print(ve)  # <-- the exception is handled here

try:
    # Converting a name to float
    float('Brian')
except ValueError as ve:  # <-- catch the IndexError
    print(ve)  # <-- the exception is handled here


