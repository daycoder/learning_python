"""
An KeyError is raised when an object doesn't
exist in a dictionary
"""

ages = {'Brian': 29,
        'Hywel': 55}

for key in ages:
    print(f"for {key=}, {ages[key]=}")

try:
    # key is not in the dictionary
    ages['Chloe']
except KeyError as ve:  # <-- catch the KeyError
    print(f'{ve} is not a key of ages')  # <-- the exception is handled here


