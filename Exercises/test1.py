name = input("enter name: ")

lastName = input("enter \' lastName: ")

name, lastName = lastName, name

print("hii: ", name[:2] + lastName * 2)
# print('({},{}),({},{})'.format(num1, num2, num1, num2))

age = input("enter age: ")
print("age *2: ", int(age) ** 2)

numbers = "123456789"

print(numbers[0:10:1])
print(numbers[3:6:3])
print(numbers[-1:-10])


def power(base, exponent):
    """Calculates a number raised to a power.
    :param base: base value
    :param exponent: exponent value
    :type base: int
    :type exponent: int
    :return: The result of raising base to the power exponent
    :rtype: int
    """
    return base ** exponent

# Old https://pyformat.info/
# '%s %s' % ('one', 'two')
# New
# '{} {}'.format('one', 'two')
# Output
# one two
# Old
# '%d %d' % (1, 2)
# New
# '{} {}'.format(1, 2)
# Output
# 1 2
