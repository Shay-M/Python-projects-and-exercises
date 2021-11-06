import random

total = 0
for i in range(4):
    cube_num = random.randint(1, 6)
    total += cube_num

print(total)

# Generator that generates 4 random numbers representing dice rolls.
cube_game = (random.randint(1, 6) for i in range(4))
total = 0
for num in cube_game:
    total += num

print(total)


#  without itertools

def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp_perm = []
        for i in range(len(seq)):
            part = seq[:i] + seq[i + 1:]
            for p in permutate(part):
                temp_perm.append(seq[i:i + 1] + p)
        return temp_perm


import itertools  # https://docs.python.org/3.6/library/itertools.html

for permutation in itertools.permutations([0, 5, 6, 9]):
    print(permutation)

# Pipelining Generators

integers = (i for i in range(1, 11))
squared = (x * x for x in integers)
negated = (-y for y in squared)
for num in negated:
    print(num)

# https://s3.eu-west-1.amazonaws.com/data.cyber.org.il/virtual_courses/next.py/data/expansion/chapter_4/%D7%A9%D7%99%D7%9E%D7%95%D7%A9%20%D7%9E%D7%AA%D7%A7%D7%93%D7%9D%20%D7%91%D7%94%D7%A6%D7%A0%D7%A8%D7%AA%20%D7%92%D7%A0%D7%A8%D7%98%D7%95%D7%A8%D7%99%D7%9D.html
