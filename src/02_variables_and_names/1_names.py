"""
In Python, variables are called names.

Not bad names, like "shit-for-brains". I mean we
often refer to variables as names. But if you say
variables instead, that's fine. Everyone will know
what you mean.

Names are just a way to hold a reference to a thing.

Names (for variables) should be lowercase and
snake_case. They can start with an underscore.
Here are some valid names:

    brian
    _property_name
    mobile_phone_number


>>> a = 2

Note that nothing prints out for a = 2.
That's ok. We just told Python to make
us an integer and to refer to it as 'a',

We can see its type and its value

>>> type(a)
<class 'int'>
>>> a
2

We can use a name to refer to anything.
And once we have a name for something, we can use
it instead of a literal. Kind of like algebra.

>>> a + 2
4
>>> ten_a = a * 10
>>> ten_a
20

But ten_a is just a snapshot.
It doesn't know about changes to a
>>> a
2
>>> a = 3
>>> a
3
>>> ten_a
20

>>> _1_000_000 = "One Million!"
>>> _1_000_000
'One Million!'
"""