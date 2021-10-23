def inverse_dict(my_dict):
    new_dict = {}
    # Index = 0

    dict_keys = list(my_dict.keys())
    dict_values = list(my_dict.values())
    # list_of_keys = my_dict.keys()
    # list_of_values = my_dict.values()

    # for value in dict_values:
    #     new_dict.setdefault(value, [])

    for value in dict_values:
        new_dict.setdefault(value, [])
        new_dict.get(value).append(dict_keys.pop(0))
        # Index = Index + 1

    return new_dict


# this_dict.setdefault(list(list_of_values).pop(), [].append("item"))
# return this_dict
# thisdict = dict.fromkeys(list_of_values, list_of_keys)
# print(thisdict)

# for i in range(len(my_dict)):

# this_dict.setdefault(list(list_of_values).pop(i), list(list_of_keys).pop(i))

# if new_dict.get(i + 1) is not None:
#     tempp = new_dict.get(i + 1)
#     # this_dict.get(i).append(this_dict.get(i))
#     tempp.append(list(list_of_keys).pop(i))
#     # this_dict.update({list(list_of_values).pop(i): list(list_of_keys).pop(i)})
#     new_dict.update({list(list_of_values).pop(i): tempp})
#     # new_list_of_values.append(this_dict.get(i, "XXX"))
#     # this_dict.setdefault(list(list_of_values).pop(i), new_list_of_values)

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))  # {3: ['I', 'love'], 2: ['self.py!']}
