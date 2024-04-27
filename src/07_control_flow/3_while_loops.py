"""
A while loop is used when you need
run some code while a condition is
True

while <condition>:
    do something

You can terminate early with break:

while <condition>
    do+something
    if <some condition>:
        break  # Ends the loop
    do_something

You can skip to the start of the loop
with continue


while <condition>
    do_something
    if <some condition>:
        continue
        # ^ jumps to the start of the loop
        # without doing "do_something_else"
    do_something_else

"""

import time

FIVE_SECONDS = 5

start_time = time.time()
print(f'{start_time=}')

time.sleep(FIVE_SECONDS)

end_time = time.time()
print(f'{end_time=}')

elapsed_time = int(end_time - start_time)

print(f'{elapsed_time=}')

# Let's use a while loop to get some feedback while we wait

start_time = time.time()
for second in range(FIVE_SECONDS):
    time.sleep(1)
    print(f'waited for {second + 1} seconds')

end_time = time.time()
print(f'{end_time=}')
elapsed_time = int(end_time - start_time)
print(f'{elapsed_time=}')

# Use a while loop instead
start_time = time.time()
countdown = FIVE_SECONDS
while countdown > 0:
    time.sleep(1)
    print(f'{countdown} seconds left')
    countdown -= 1

end_time = time.time()
print(f'{end_time=}')
elapsed_time = int(end_time - start_time)
print(f'{elapsed_time=}')


# Use a while and monitoring elapsed time
start_time = time.time()
time_left = FIVE_SECONDS
while time_left > 0:
    time.sleep(0.5)
    now = time.time()  # glance at the clock
    elapsed_time = now - start_time
    time_left = FIVE_SECONDS - elapsed_time
    print(f'{time_left} seconds left')
    pass


end_time = time.time()
print(f'{end_time=}')
elapsed_time = int(end_time - start_time)
print(f'{elapsed_time=}')


# Use a while and monitoring elapsed time
start_time = time.time()
time_left = FIVE_SECONDS
while True:
    time.sleep(0.5)
    now = time.time()  # glance at the clock
    elapsed_time = now - start_time
    time_left = FIVE_SECONDS - elapsed_time
    if time_left < 0:
        break  # stop the loop
    print(f'{time_left} seconds left')
    pass


end_time = time.time()
print(f'{end_time=}')
elapsed_time = int(end_time - start_time)
print(f'{elapsed_time=}')