"""
Integers are just whole numbers.

You can write them as decimal, hex, octal, or binary.
You can add underscores to make big numbers more
readable

>>> 32
32
>>> 0x20
32
>>> 0x40
64
>>> type(32)
<class 'int'>
>>> type(0x20)
<class 'int'>
>>> type(0o40)
<class 'int'>
>>> int(0b0010_1000)
40
>>> type(0b0010_1000)
<class 'int'>
>>> 1_000_000
1000000
>>> type(1_000_000)
<class 'int'>

You might come across the term 'literal'.
All the integers above are literals meaning
they just a number. Other types can have
literals too. True is a boolean literal.

You can't start you decimal with a 0 or
an underscore though :(

>>> 0_000_000_1
  File "<stdin>", line 1
    0_000_000_1
    ^^^^^^^^^^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> _000_000_1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_000_000_1' is not defined


"""

# From teams chat:
# hex(20) = 0*16^0 + 2 *16^1
# = 0 + 2*16 = 32

