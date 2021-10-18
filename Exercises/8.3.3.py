def count_chars(my_str):
    this_dict = {}

    for later in my_str:
        if later != ' ':
            this_dict.update({later: my_str.count(later)})
    return this_dict


magic_str = "abra cadabra"

print(count_chars(magic_str))
