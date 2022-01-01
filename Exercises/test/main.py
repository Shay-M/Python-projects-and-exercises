def fun():
    return


print(fun())  # None


#########################
# https://www.geeksforgeeks.org/program-to-find-whether-a-given-number-is-power-of-2
# Given an integer n. return true if it is a power of two. Otherwise, return false

def is_Power_Of_Two(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2

    return True


def is_power_of_two_bit(n):
    print(n & (n - 1))
    return n and (not (n & (n - 1)))


print(is_power_of_two_bit(2))


def is_power_of_two_rec(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False

    return is_power_of_two_rec(n / 2)


numbers_for_test = [0, 1, 2, 4, 6, 8, 16, 256]

for x in numbers_for_test:
    print(x, is_power_of_two_rec(x))

# const isPnurufTquec = (mun) => {
# H (mm =:= a) return false;
# if (num === 1) return tr‘UE; :
# if (mm x 2 1:: a) return false;
# return isPolerUfTqunc(num null / 2)


msg_splited = [1, 2]
# msg_splited = ["1", "2"]
words_from_sentence = '#'.join(str(e) for e in msg_splited)

print()
print(msg_splited)

# ''.join()

print(words_from_sentence)



