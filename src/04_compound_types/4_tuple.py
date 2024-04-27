"""
IMMUTABLE!

Usually inside (), e.g. (1, 2, 3)

Kind of look like lists, but they can't be altered

>>> type((1, 2, 4))
<class 'tuple'>
>>> t = (1, 2, 3)
>>> t[0]
1
>>> t[-1]
3
>>> t[:]
(1, 2, 3)
>>> t[1:]
(2, 3)

>>> t + (1,)
(1, 2, 3, 1)
>>> t2 = t + (1,)
>>> id(t)
4333909312
>>> id(t2)
4333425344

>>> i = 1
type(i)
<class 'int'>
>>> t3 = 1,  # that , made it a tuple
>>> type(t3)
<class 'tuple'>


>>> l = [1,2,3]
>>> t = (1, 3, l)
>>> l[0] = False
>>> id(t[2])
4333186240
>>> id(l)
4333186240
>>> t[0] = False
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

"""

