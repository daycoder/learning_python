"""
A NameError is raised when a name
doesn't exist.

Note: a name is the same as a variable
"""

try:
    total  # <--using total before it's been defined
except NameError as ne:  # <-- catch the IndexError
    print(ne)  # <-- the exception is handled here


