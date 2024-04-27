"""
TODO! This is copied from file

Use a context manager to read files.
You can recognise a context manager
by the 'with' statement.
"""

with open(file="lorem_ipsum.txt", mode="r", encoding="utf-8") as lorem_ipsum:
    contents = lorem_ipsum.read()

print(contents)


# use readlines() to split the file into a list of lines
with open(file="lorem_ipsum.txt", mode="r", encoding="utf-8") as lorem_ipsum:
    lines = lorem_ipsum.readlines()


print(lines)
print(len(lines))


# Note: outside the with you can no longer access
#       the file as shown here:
try:
    lorem_ipsum.wread()
except ValueError as e:
    # The context manager (with) closed the file
    # Se we can't read from it
    print(e)