"""
Use <, <=, >, >= operands to compare values

>>> 1 < 2
True
>>> 2 < 1
False
>>> 1 < 1
False


>>> 1 <= 2
True
>>> 2 <= 1
False
>>> 1 <= 1
True


>>> 2 > 1
True
>>> 1 > 2
False
>>> 2 > 2
False


>>> 2 >= 1
True
>>> 1 >= 2
False
>>> 1 >= 1
True

>>> a = 1
>>> a > 0 and a <= 10
True

>>> a = 0
>>> a > 0 and a <= 10


>>> a = 10
>>> a > 0 and a <= 10
True

We can do this in a better way using chained operators...

>>> a = 0
>>> 0 < a <= 10
False

>>> a = 1
>>> 0 < a <= 10
True

>>> a = 10
>>> 0 < a <= 10
True

>>> a = 11
>>> 0 < a <= 10
False

Note: Convention in Python is to not have unnnecesary brackets
      Don't do this if you don't need to: ((a > 0) and (a <= 10))
      See PEP8 https://peps.python.org/pep-0008/

TODO: Get good example for logical operatro order (and vs or)
"""

