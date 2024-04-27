"""
ONe way you can control the flow of your program
is using if statements. This allows execution of
one path though the code instead of another.
"""

if True:
    print(True)

if False:
    print(False)

a = 10
# a is 10, so it'll go through the if True path
if a == 10:
    print('a is 10')
else:
    print("a is not 10!")

# a is not 9, so it'll go through the else path
if a == 9:
    print('a is 9')
else:
    print("a is not 9!")

# check a is in range 0..100
a = -1
if a < 0:
    print(f'{a=} is too low')

a = 1000
if a < 0:
    print(f'{a=} is too low')
else:
    print(f'{a=} is not too low')


if a > 100:
    print(f'{a=} is too high')
else:
    print(f'{a=} is not too high')

if a < 0:
    print(f'{a=} is too low')
elif a > 100:
    print(f'{a=} is too high')
else:
    print(f'{a=} is just right')


for a in (-1, 0, 99, 100, 101, 1000):
    if a < 0:
        print(f'{a=} is too low')
    elif a > 100:
        print(f'{a=} is too high')
    else:
        print(f'{a=} is just right')

