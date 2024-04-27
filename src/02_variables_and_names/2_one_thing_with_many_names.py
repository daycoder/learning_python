"""
THIS IS IMPORTANT:
A thing can be referred to by many names.
As long as it has a name, it exists.
If it no longer has a name, it'll be discarded.

Like the same person "Brian" can be a father
and a son.
>>> brian = 'Brian'
>>> father = brian
>>> son = brian
>>> father
'Brian'
>>> son
'Brian'
>>> brian
'Brian'

We can throw away one of the names (with the del command),
and the other names are still good

>>> del son
>>> son
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'son' is not defined
>>> brian
'Brian'
>>> father
'Brian'

You can use a name to refer to something different and it
will not affect what other names refer to:

>>> father = "Father"
>>> father
'Father'
>>> brian
'Brian'

"""