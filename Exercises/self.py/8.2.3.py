first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)


def mul_tuple(tuple1, tuple2):
    temp_list = []
    for num1 in tuple1:
        for num2 in tuple2:
            temp_tuple = (num1, num2)
            temp_list.append((num1, num2))
            temp_list.append((num2, num1))
    return temp_list


print(mul_tuple(first_tuple, second_tuple))
