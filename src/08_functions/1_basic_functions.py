"""

"""
a = 1  # scope of this a is global


def print_value(a):
    print(f'{a=}')

print_value(a)


def print_double(value):
    a = 2  # Scope if this a is inside double only
    print(f'{locals()=}')
    print(f'{globals()=}')
    print(f'{value * 2=}')

print_double(a)


def double(value):
    return value * 2


print(f'{double(4)=}, {(double(4) == 8)=}')


def use_global_a(value):
    global a  # force using the global a
    a = 2  # Scope if this a is inside double only
    print(f'{locals()=}')
    print(f'{globals()=}')
    print(f'{value * 2=}')

use_global_a(4)


# Let's turn this in to a function...
for test_datum in (-1, 0, 99, 100, 101, 1000):
    if test_datum < 0:
        print(f'{a=} is too low')
    elif test_datum > 100:
        print(f'{test_datum=} is too high')
    else:
        print(f'{test_datum=} is just right')


def print_is_valid_percent_value(percent):
    if percent < 0:
        print(f'{percent=} is too low')
    elif percent > 100:
        print(f'{percent=} is too high')
    else:
        print(f'{percent=} is just right')


for test_datum in (-1, 0, 99, 100, 101, 1000):
    print_is_valid_percent_value(test_datum)


# Functions can return values
def is_valid_percent_value(number):
    """
    Returns True if number between 0 and 100
    :param number: integer or float
    :return: bool
    """
    if 0 <= number <= 100:
        return True
    else:
        return False


test_data = {-1: False,
             0: True,
             99: True,
             100: True,
             101: False,
             1000: False}
"""
>>> test_data.keys()
dict_keys([-1, 0, 99, 100, 101, 1000])
>>> test_data.values()
dict_values([False, True, True, True, True, True])
>>> test_data.items()
dict_items([(-1, False), (0, True), (99, True), (100, True), (101, True), (1000, True)])

unpacking tuples...
>>> key_value_pair_in_tuple = ('x', 'twitter')
>>> key, value = key_value_pair_in_tuple
>>> key
'x'
>>> value
'twitter'
(This is the same:)
>>> key, value =  ('x', 'twitter')
"""

# Test the is_valid_percent_value function
for value, expected in test_data.items():
    result = is_valid_percent_value(value)
    if result == expected:
        print(f'PASSED! {result=} for {value=}. {expected=}')
    else:
        print(f'FAIL! {result=} for {value=}. {expected=}')


# You can pass many parameters to a function
def full_name(forenames: str, surname: str) -> str:
    """
    Joins forenames and surname string
    """
    result = f'{forenames} {surname}'
    return result

# You can test your code using assert statements
assert True, "All fine"
try:  # We'll do more on exception handling later!
    assert False, "Something went wrong"
except AssertionError:
    print('caught the assert False safely')

# No names for parameter so uses the order defined in the function
brian_ferry = full_name("Brian",
                        "Ferry")
assert brian_ferry == "Brian Ferry",  f'{brian_ferry=} Expected = "Brian Ferry"'
print(f'{brian_ferry=}')

# use named parameters to be explicit and not rely on parameter order
nicola_bracanto = full_name(surname="Bracanto",
                            forenames="Nicola")
assert nicola_bracanto == "Nicola Bracanto",  f'{nicola_bracanto=} Expected = "Nicola Bracanto"'
print(f'{nicola_bracanto=}')


# default parameter values.
# You don't have to pass that parameter!
def increment(value,
              inc=1,
              ):  # This is the default value
    result = value + inc
    return result


assert increment(-1) == 0, "-1 should have incremented to 0"
assert increment(0) == 1, "0 should have incremented to 1"
assert increment(4, 5) == 9, "4 should have incremented to 9"


# A function only returns one thing, but that thing can be
# anything, *including* a tuple, which is how we commonly
# return multiple values ...

def swap(a, b) -> tuple:
    return (b, a)

swapped = swap('x', 123.456)

assert swapped == (123.456, 'x')
assert type(swapped) == tuple


# *REALLY* subtle difference. We're not using () on the tuple
def swap2(a, b) -> tuple:
    return b, a

swapped2 = swap2('x', 123.456)
assert swapped2 == (123.456, 'x')
assert type(swapped2) == tuple

# WARNING! It's really easy to accidentally define tuples
accidental_tuple = "Brian",  # Doesn't need ()
assert type(accidental_tuple) == tuple

swapped2 = swap2('x', 123.456)
assert swapped2 == (123.456, 'x')
assert type(swapped2) == tuple

# unpack a returned tuple into a tuple!
# many values returned can go into many names/variables
first, second = swap2('x', 123.456)
assert first == 123.456
assert second == 'x'
assert type(first) == float
assert type(second) == str

# assert reminder..
assert second == 'x'
# is equivalent to:
if not(second == 'x'):
    raise AssertionError(f'{second=}, expected "x"')