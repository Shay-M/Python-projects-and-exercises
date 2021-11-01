import functools

list_one = [1, 2, -5, 6]
list_two = [2, -1, 3, 4]


# --------------map------------------------------------

def magic(a, b):
    return a * b


print(list(map(magic, list_one, list_two)))  # [2, -2, -15, 24]


# -------------filter-------------------------------------

def func(x):
    return x % 2 != 0


print(list(filter(func, range(10))))  # [1, 3, 5, 7, 9]


# -------------functools.reduce---------------------------


def f(a, b):
    if a < b:
        return a
    else:
        return b


print(functools.reduce(f, [47, 11, 42, 102, 13]))  # 11


# ------------------------------------------------------
# functools.reduce(function, sequence[, initializer])

def add(x, y):
    return x + y


shopping_list = [200, 120, 330, 50]
print(functools.reduce(add, shopping_list, 15))  # 715


# -1.1.1-----------------------------------------------------
def secret(a):
    return a % 3 != 0 and a % 5 != 0


result = filter(secret, range(1, 31))
print(list(result))  # [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29]


# -1.1.2-----------------------------------------------------


def double_l_map(args):
    return args * 2


def double_letter(my_str):
    return ''.join(list(map(double_l_map, my_str)))


print(double_letter("python"))  # ppyytthhoonn
print(double_letter("we are the champions!"))  # wwee  aarree  tthhee  cchhaammppiioonnss!!


# -1.1.3-----------------------------------------------------
def try_dividers_by_fore(number):
    return number % 4 == 0


def four_dividers(number):
    return list(filter(try_dividers_by_fore, range(1, number)))


print(four_dividers(9))  # [4, 8]
print(four_dividers(3))  # []


# 1.1.4----------------for not good--------------------------------


def sum_of_digits1(number):
    return sum(int(i) for i in str(number))


print(sum_of_digits1(104))


# -good way-----------------------------------

def sd(a, b):
    return int(a) + int(b)


def sum_of_digits(number):
    return functools.reduce(sd, str(number))


print(sum_of_digits(1041))  # 6

# -------------lambda-----------------------------------
print((lambda y, x: x in y)([1, 5, 6, 9], 9))  # true

# Sort the toppings according to the numerical value in the organ in the second position in each toppings.
list_of_tuples = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(sorted(list_of_tuples, key=lambda x: x[1]))  # [(4, 1), (2, 2), (1, 3), (3, 4)]

calc_sqrt_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for func in calc_sqrt_list:
    print(func(3))


#  9
# 27
# 81

# ------------------------------------------------------


def function(num, item):
    return num + 1  # num + item


password = "123"  # input("Enter Your password (integers only): ")  # 16
lst = list(map(int, password))

print(lst)  # [1, 6]

magic = functools.reduce(function, lst)
print(magic)  # 2
result = (lambda x: x % 4 == 0)(magic)

print(result)

# ------------------------------------------------------
list1 = [1, 2, 3]
list2 = [5, 6, 7]
mult_list = [x * y for x in list1 for y in list2]
print(mult_list)  # [5, 6, 7, 10, 12, 14, 15, 18, 21]

nested_list = [x * 2 for x in range(10) if x > 3 if x < 7]
print(nested_list)  # [8, 10, 12]

even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(even_odd_list)  # ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

numbers = [1, 2, 3, 4]
list_of_lists = [[2 * x, x] for x in numbers]
print(list_of_lists)  # [[2, 1], [4, 2], [6, 3], [8, 4]]

sentence = "the quick brown fox"
words = sentence.split()
secret = [word[0] for word in words if word != "the"]
print(secret)  # ['q', 'b', 'f']

# https://book.pythontips.com/en/latest/comprehensions.html

# ------------------------------------------------------
print("_________combine_coins_________")


def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
    # Ignore the last comma.
    return output[:-2]


print(combine_coins('$', range(5)))  # $0, $1, $2, $3, $4


def one_line_combine_coins(coin, numbers_s): return ', '.join([coin + str(i) for i in numbers_s])  # $0, $1, $2, $3, $4


# def one_line_combine_coins(coin, numbers): return [coin + str(num) for num in numbers]
# not good ['$0', '$1', '$2', '$3', '$4']


print(one_line_combine_coins('$', range(5)))  # $0, $1, $2, $3, $4

# --------------------------------------------------------

power_3_list = []
for i in range(100):
    power_3_list.append(i ** 3)
print(power_3_list)

# good way
power_3_list = [i ** 3 for i in range(100)]
print(power_3_list)

# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261,
# 10648, 12167, 13824, 15625, 17576, 19683, 21952, 24389, 27000, 29791, 32768, 35937, 39304, 42875, 46656, 50653,
# 54872, 59319, 64000, 68921, 74088, 79507, 85184, 91125, 97336, 103823, 110592, 117649, 125000, 132651, 140608,
# 148877, 157464, 166375, 175616, 185193, 195112, 205379, 216000, 226981, 238328, 250047, 262144, 274625, 287496,
# 300763, 314432, 328509, 343000, 357911, 373248, 389017, 405224, 421875, 438976, 456533, 474552, 493039, 512000,
# 531441, 551368, 571787, 592704, 614125, 636056, 658503, 681472, 704969, 729000, 753571, 778688, 804357, 830584,
# 857375, 884736, 912673, 941192, 970299]

# # ------------------------------------------------------
list1 = [1, 2, 3]
list2 = [5, 6, 7]
mult_list = [x * y for x in list1 for y in list2]

print(mult_list)  # [5, 6, 7, 10, 12, 14, 15, 18, 21]

# # ------------------------------------------------------
nested_list = [x * 2 for x in range(10) if x > 3 if x < 7]
print(nested_list)  # [8, 10, 12]

# # ------------------------------------------------------
# Note that in such a case, where we want to perform another
# action for the non-fulfilling condition, the condition commands and the actions to perform are written before the
# loop.

even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]

print(even_odd_list)  # ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

# # ------------------------------------------------------

