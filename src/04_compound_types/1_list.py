"""
>>> []
[]
>>> type([])
<class 'list'>
>>> [1, 2, 'x', 2]
[1, 2, 3, 'x']
>>> type([1, 2, 'x', 2])
<class 'list'>

You can join two lists:

>>> [1, 2, "x", 2] + [3]
[1, 2, 'x', 2, 3]

But you can't join a list with something else:

>>> [1, 2, "x", 2] + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list

To do useful things with a list, we need to store it
in a variable.

>>> some_list = [1, 2.0, '3', False, None]
>>> some_list
[1, 2.0, '3', False, None]

>>> len(some_list)
5

>>> some_list.append('Brian')
>>> some_list
[1, 2.0, '3', False, None, 'Brian']

>>> some_list[0]
1

>>> some_list[-1]
'Brian'

>>> some_list[6]
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
IndexError: list index out of range

>>> some_list[-1][0]
'B'

>>> another_list.append('x')

>>> another_list = [1,1,1,1,1,1]
>>> some_list.append(another_list)

>>> some_list[0] = 100
>>> some_list[0]
100
>>> some_list.index('Brian')
5

>>> some_list.pop()
[1, 1, 1, 1, 1, 1, 'x']
>>> some_list.append(another_list)
>>> some_list.pop(0)
100
>>> some_list.pop(some_list.index('Brian'))
'Brian'

>>> yet_another_list = ['a','b','c']
>>> some_list.extend(yet_another_list)
>>> some_list
[2.0, '3', False, None, [1, 1, 1, 1, 1, 1, 'x'], 'a', 'b', 'c']

>>> some_list[0:2]
[2.0, '3']
>>> some_list[2:3]
[False]
>>> some_list[2:4]
[False, None]

>>> some_list[1:-1]
['3', False, None, [1, 1, 1, 1, 1, 1, 'x'], 'a', 'b']
>>> some_list[1:]
['3', False, None, [1, 1, 1, 1, 1, 1, 'x'], 'a', 'b', 'c']

>>> l = [1, 2, 3, 67, 44]
>>> l
[1, 2, 3, 67, 44]
>> id(l)
4339729280
>>> l[:]  # Use slice [:] to make a (shallow) copy
[1, 2, 3, 67, 44]
>>> id(l[:])
4340903680
"""