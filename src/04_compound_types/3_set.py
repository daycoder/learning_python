"""
Sets look a lot like lists, but they're immutable.
You can't modify them.
It contains only unique values (no duplicates)

>>> {1, 2, 4, "Brian"}
{1, 2, 4, 'Brian'}
>>> type({1, 2, 4, "Brian"})
<class 'set'>

Trying to use duplicate values
>>> {1, 2, 4, "Brian", 1, 2, 1}
{1, 2, 4, 'Brian'}

Sets are useful for stuff like finding how
many unique values are in a list
>>> [1, 2, 4, "Brian", 1, 2, 1]
[1, 2, 4, 'Brian', 1, 2, 1]
>>> set([1, 2, 4, "Brian", 1, 2, 1])
{1, 2, 4, 'Brian'}
len(set([1, 2, 4, "Brian", 1, 2, 1]))
4

More to discover, like differences, union etc
"""