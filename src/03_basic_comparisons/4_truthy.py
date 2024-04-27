"""
There's a concept in Python where objects
have a 'truthiness'

These values resolve to False:

    0
    0.0
    False
    None
    ""
    []  - empty list
    ()  - empty set
    {}  - empty dictionary

Everything else resolves to True

i.e.
>>> a = 0
>>> bool(a)
False

>>> b = -1
>>> bool(b)
True

>>> c = 3.142
>>> bool(c)
True

"""