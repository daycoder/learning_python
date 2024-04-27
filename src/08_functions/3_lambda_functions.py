# You can write small functions using this shortcut

# Syntax is:
# lambda <params>: <body>
#
# <body> has to fit in one statement

double = lambda value: value * 2
"""
>>> double
<function <lambda> at 0x1049dd310>
>>> type(double)
<class 'function'>
"""

assert double(4) == 8
print(f'{double(4)=}')


# The lambda function is exactly the same as doing this:
def double(value):
    return value * 2


# Often used in sorting stuff!
list_of_dicts = [
    {'name': "Brain", 'age': 60},
    {'name': "Nicola", 'age': 29},
    {'name': "Hywel", 'age': 55},
]

# Can't sort a list of dictionaries
try:
    list_of_dicts.sort()
except TypeError:
    print("Can't sort a list of dictionaries")


# Let's sort this by age
list_of_dicts.sort(key=lambda d: d['age'])

# Let's sort this by name
list_of_dicts.sort(key=lambda d: d['name'])

# What the hell just happened?

get_age_lambda = lambda d: d['age']
print(f'{get_age_lambda=}')
print(f'{(list_of_dicts[0])=}')
print(f'{(list_of_dicts[0]["age"])=}')
print(f'{get_age_lambda(list_of_dicts[0])=}')


# # The lambda function is exactly the same as doing this:
def get_age_from_def_function(d):
    return d['age']

print(f'{get_age_from_def_function(list_of_dicts[0])=}')
pass