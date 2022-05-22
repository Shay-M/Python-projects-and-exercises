# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# https://www.youtube.com/watch?v=YPTqKIgVk-k

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2] | O(n)

from collections import Counter


nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequentFastWay(nums, k):

    res = []
    for key in Counter(nums).most_common(k):
        # print(key)
        # (1, 3)
        # (2, 2)
        res.append(key[0])  # 1, 2 keys are the most common

    return res


print(topKFrequentFastWay(nums, k))

# --------------------------------------------------------------------------------


def topKFrequent(nums, k):
    count = {}

    #  freq = [[]] * (len(nums) + 1)
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:  # 1,1,1,2,2,3
        # get count with the key 'n' if not have any it is 0
        count[n] = 1 + count.get(n, 0)

    # print(count)  #//* count : {1: 3, 2: 2, 3: 1}   # print(count.get(1))  # 3

    for n, c in count.items():
        # 1 3
        # 2 2
        # 3 1
        freq[c].append(n)

    print(freq)  # //* [[], [3], [2], [1], [], [], []]

    # now we finished initial!

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent(nums, k))
