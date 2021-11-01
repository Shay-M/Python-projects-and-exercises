# import functools


# --1.3.1---------------------------------------------------
# https://www.datacamp.com/community/tutorials/sets-in-python

def intersection(list_1, list_2):
    return [a for a in set(list_1) if a in set(list_2)]
    # return list(set(list_1).intersection(set(list_2))) # optional


print(intersection([1, 2, 3, 4], [8, 3, 9]))  # [3]
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))  # [5,6]

# --1.3.2---------------------------------------------------
print('-- 1.3.2')


def is_prime(number):
    return [num for num in range(2, int(number ** 0.5)) if number % num == 0] == []


print(is_prime(42))
print(is_prime(43))

# --1.3.3---------------------------------------------------
print('-- 1.3.3')


def is_funny_long_way(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True


def is_funny(string):
    return [char for char in string if char != 'h' and char != 'a'] == []


print(is_funny("hahahahahaha"))

# --1.3.4---------------------------------------------------
print('-- 1.3.4')

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


def password_uncode(password):
    return ''.join([chr(ord(char) + 2) if char.isalpha() else char for char in password])


print(password_uncode(password))
# --1.4---------------------------------------------------
print('-- random.choice')
import random

p = lambda: random.choice('7♪♫♣♠♦♥◄☼☽')
[print('|'.join([p(), p(), p()]), end='\r') for i in range(8 ** 5)]

