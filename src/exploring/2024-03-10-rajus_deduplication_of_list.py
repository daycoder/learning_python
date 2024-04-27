def remove_duplicates_from_list(num_list):
    duplicates_removed_list = []
    for num in num_list:
        if num not in duplicates_removed_list:
            duplicates_removed_list.append(num)
    return duplicates_removed_list


test_num_list = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
id_before_function = id(test_num_list)
test_num_list = remove_duplicates_from_list(test_num_list)
id_after_function = id(test_num_list)
assert id_before_function != id_after_function  # id changes. new list
print(test_num_list)


# -----------------------------------------------------------------------------


def remove_duplicates_in_place(num_list):
    index_of_numbers = {}
    for index, num in enumerate(num_list):
        if num in index_of_numbers:
            index_of_numbers[num].append(index)
        else:
            index_of_numbers[num] = [index]
    for number, indices in reversed(index_of_numbers.items()):
        for index in reversed(indices[1:]):
            del num_list[index]


test_num_list_2 = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
id_before_function = id(test_num_list_2)
remove_duplicates_in_place(test_num_list_2)

id_after_function = id(test_num_list_2)
assert id_before_function == id_after_function # id is the same. Not a new list

# -----------------------------------------------------------------------------

# Improve on the [1:] but not storing the first hit ...


def remove_duplicates_in_place(num_list):
    index_of_numbers = {}
    for index, num in enumerate(num_list):
        if num in index_of_numbers:
            index_of_numbers[num].append(index)
        else:
            index_of_numbers[num] = []  # <- better
    for number, indices in reversed(index_of_numbers.items()):
        for index in reversed(indices):
            del num_list[index]


test_num_list_2 = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
id_before_function = id(test_num_list_2)
remove_duplicates_in_place(test_num_list_2)

id_after_function = id(test_num_list_2)
assert id_before_function == id_after_function # id is the same. Not a new list


# -----------------------------------------------------------------------------


def remove_duplicates_in_place_with_pop(num_list):
    found_numbers = []
    for index, num in reversed(list(enumerate(num_list))):
        if num in found_numbers:
            num_list.pop(index)
        else:
            found_numbers.append(num)


test_num_list_3 = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
id_before_function = id(test_num_list_3)
remove_duplicates_in_place_with_pop(test_num_list_3)
id_after_function = id(test_num_list_3)
assert id_before_function == id_after_function  # id is the same. Not a new list
