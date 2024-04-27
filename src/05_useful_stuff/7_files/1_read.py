"""
Use a context manager to read files.
You can recognise a context manager
by the 'with' statement.

with open() as name:
   name.<method()>

open() opens a file.
mode='r' means read.
encoding='utf-8' is what you usually want to use!

"""

# Without a context manager (with). DO NOT DO THIS!
lorem_ipsum = open(file="lorem_ipsum.txt", mode="r", encoding="utf-8")
contents = lorem_ipsum.read()
more = lorem_ipsum.read()  # No error!
lorem_ipsum.close()
print(contents)
print(f'{more=}')

# use read() to read the whole file as a single string
with open(file="lorem_ipsum.txt", mode="r", encoding="utf-8") as lorem_ipsum:
    contents = lorem_ipsum.read()
    more = lorem_ipsum.read()  # safe inside the with

try:
   even_more = lorem_ipsum.read()  # safe inside the with
except ValueError as value_error:
    print(f"Get '{value_error}' because the with context manager closed the file")

print(contents)
print(f'{more=}')


# use readlines() to split the file into a list of lines
with open(file="lorem_ipsum.txt", mode="r", encoding="utf-8") as lorem_ipsum:
    lines = lorem_ipsum.readlines()


print(lines)
print(len(lines))


# use readline() to read one line at a time
with open(file="lorem_ipsum.txt", mode="r", encoding="utf-8") as lorem_ipsum:
    line = lorem_ipsum.readline()  # will have a \n at the end
    print(f"{line=}")

print(line)
print('end')