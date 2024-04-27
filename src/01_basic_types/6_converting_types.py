"""
You can often convert one type to another.

>>> type('1')
<class 'str'>
>>> int('1')
1
>>> type('1.9')
<class 'str'>
>>> float('1.9')
1.9
>>> int(1.9)
1

int(1.9) returning 1 might seem strange.
Maybe you expected it to round up to 2?
In that case you'd need to use a build in
function:
>>> round(1.4)
1
>>> round(1.5)
2

Sometimes you can't convert at all because python doesn't
quite know what you want to do:

>>> int('1.9')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.9'

How do we solve this?

>>> float(1)
1.0
>>> type(float(1))
<class 'float'>

>>> float("1.9")
1.9
>>> int(float("1.9"))
1
>>> round(float("1.9"))
2

Converting stringgs to boolean might suprise you.
And empty string gets cvonverted to False.
A non empty string, even if its "False", gets
converted to True

>>> bool('True')
True
>>> bool('true')
True
>>> bool('False')
True
>>> bool('')
False

Converting ASCII characters from/to integers

integer to character
>>> chr(65)
'A'
>>> type(chr(65))
<class 'str'>

character to integer
>>> ord('A')
65
>>> type(ord('A'))
<class 'int'>
"""