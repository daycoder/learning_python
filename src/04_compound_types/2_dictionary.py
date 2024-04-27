"""
Dictionaries also known hashes and ?
These are containers for key: value pairs

>>>my_dict = {1: "One"}
>>> my_dict
{1: 'One'}

Can't access with an index, only keys
>>> my_dict[0]
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
KeyError: 0

>>> my_dict[1]
'One'
>>> my_dict[2] = "Two"
>>> my_dict["3"] = "Three"
>>> my_dict["3"]
'Three'
>>> del my_dict["3"]
>>> another_dict = {'brian': 'Brian Jacks'}
>>> another_dict['Fred'] ='Fred Dibnah'
>>> another_dict
{'brian': 'Brian Jacks', 'Fred': 'Fred Dibnah'}


Use get instead of [key]:
>>> my_dict = {1: 'One', 2: 'Two', 'l': [1, 2, 4], 4: 'Four'}
>>> my_dict['brian']
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
KeyError: 'brian'
>>> my_dict.get('brian')
>>> print(my_dict.get('brian'))
None
>>> print(my_dict.get('l'))
[1, 2, 4]
>>> my_dict.get('brian', 'ABSENT')
'ABSENT'
"""