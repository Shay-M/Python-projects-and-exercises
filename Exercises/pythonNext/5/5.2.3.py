import itertools
import time

counter = itertools.count(start=0)
wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
wallet.sort(reverse=True)

start = time.time()

for i in range(1, len(wallet)):
    money_iter = list(itertools.combinations(wallet, i))
    # print(money_iter)
    comb = set(money_iter)
    # print(comb)

    for X in comb:
        if sum(X) == 100:
            print(X)

print(f'Time: {time.time() - start}')
##########################################

start = time.time()

result = [seq for i in range(len(wallet), 0, -1) for seq in itertools.combinations(wallet, i) if sum(seq) == 100]
# print(list(dict.fromkeys(result)))
print(list(set(result)))

print(f'Time: {time.time() - start}')
