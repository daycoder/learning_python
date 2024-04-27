"""
Syntax is for item in items:
"""

my_list = [1, 2, 3, 8, 'x']

print(my_list[0])
print()

# Don't use range/index if you don't need to
for index in range(len(my_list)):
    print(f'{index + 1}: {my_list[index]}')

# loop over the object instead
for item in my_list:
    print(item)

# But if you do want the index, use enumarate instead
for index, item in enumerate(my_list):
    print(f'{index + 1}: {item}')

names = ('Brian', 'Fred', 'Hywel', 'Hitler', 'Jesus')

for name in names:
    print(name)
    # Nested loop
    for character in name:
        print(character)

# break out of a loop. Stop a loop early
for name in names:
    if name == "Hitler":
        break
    print(name)

# To jump straight to the next iteration of a loop
# use continue
for name in names:
    if name == "Hitler":
        continue
    print(name)
