def get_fibo():
    yield 0
    yield 1
    n1 = 1
    n2 = 0
    while True:
        sum = n1 + n2
        n2 = n1
        n1 = sum
        yield sum


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
