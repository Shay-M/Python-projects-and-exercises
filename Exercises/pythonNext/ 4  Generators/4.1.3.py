import time
from itertools import count


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(num):
    if num < 0:
        return 2

    prime_generator = (n for n in range(num + 1, num * 2, 1) if is_prime(n))
    # num + 1, --> start from n+1
    # num * 2, --> Bertrand's postulate : https://en.wikipedia.org/wiki/Bertrand%27s_postulate
    # 2        --> Skip even numbers
    return next(prime_generator)


def first_prime_over2(n):
    offset = 1 if n % 2 == 0 else 2
    return next((a for a in count(n + offset, 2) if is_prime(a)))


start = time.time()

# print(first_prime_over2(1000000)) # Time: 0.05829763412475586
print(first_prime_over(1000001))  # Time: 0.05780506134033203

print(f'Time: {time.time() - start}')
