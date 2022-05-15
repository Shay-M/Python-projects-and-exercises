# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2] |  O(n)

nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequent(nums, k):
    count = {}
    freq = [[]] * (len(nums) + 1)

    for n in nums:  # 1,1,1,2,2,3
        # get count with the key 'n' if not have any it is 0
        count[n] = 1 + count.get(n, 0)
    # count : {1: 3, 2: 2, 3: 1}
    print(count)
    print(count.get(1))  # 3

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent(nums, k))
