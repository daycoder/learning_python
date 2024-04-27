"""
<class 'str'>

Strings are containers for 0 or more characters/letters

In Python, they are unicode, so characters can be any unicode value, like '(◕‿◕)'

You define thenm with single quotes '
                   or double quotes "
>>> 'c'
'c'
>>> type('c')
<class 'str'>

>>> "(◕‿◕) Has unicode characters"
'(◕‿◕) Has unicode characters'

>>> "this is a string in double quotes"
'this is a string in double quotes'

>>> "the start quote must match the end quote'
Traceback (most recent call last):
  File "<input>", line 1
    "the start quote must match the end quote'
  ...                                       ^
SyntaxError: EOL while scanning string literal

>>> "It's ok to put a single quote in thie double quoted string"
"It's ok to put a single quote in thie double quoted string"

>>> 'You can put a "double quote" inside a single quoted string'
'You can put a "double quote" inside a single quoted string'

You can also use triple quoted strings that span mulitple lines
just like this one

You'll see \n used a lot in strings. This just means new line.
>>> '\nline \'1\'\nline "2"\n\nline \'4"\n'
'\nline \'1\'\nline "2"\n\nline \'4"\n'

>>> print('\nline \'1\'\nline "2"\n\nline \'4"\n')

line '1'
line "2"

line '4"

>>>
"""

"""
line '1'
line "2"

line '4"
"""