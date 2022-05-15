# Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is
# [2,3,7,101], ^ therefore the length is 4.

import bisect  # for Using Binary Search

arr = [10, 9, 2, 5, 3, 7, 101, 18]


def lengthOfLIS(nums):
    LIS = [1] * len(arr)

    # for i in range(len(nums)):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             LIS[i] = max(LIS[i], 1 + LIS[j])
    # print('LIS: ', LIS)
    # return max(LIS)

    # /# for i in range(start, stop at - 1 so 0 to do, step)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    print('LIS: ', LIS)
    return max(LIS)


print(lengthOfLIS(arr))

# -----------------------------------
# Using Binary Search


def lengthOfLISBinarySearch(nums):
    l = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > l[-1]:
            l.append(nums[i])
        else:
            l[bisect.bisect_left(l, nums[i])] = nums[i]

    return len(l)


print(lengthOfLISBinarySearch(arr))

# without import bisect
# this binarySearch function returns the index of the element if it is present. If the element is
# not present it returns the index of the 'next greater element' For example arr=[1,7,8,9]and
# n=4. Since 4 is not present in the array it will return 1, which is the index of next greater
# element of 4 i.e., 7


def lengthOfLISBinarySearchWithout(nums):
    def binarySearch(arr, n):
        st = 0
        ed = len(arr)-1
        while st <= ed:
            mid = (st+ed)//2
            if arr[mid] == n:
                return mid
            elif arr[mid] > n:
                ed = mid-1
            else:
                st = mid+1
        return st

    ans = []
    ans.append(nums[0])
    for i in range(1, len(nums)):
        if ans[-1] < nums[i]:
            ans.append(nums[i])
        else:
            idx = binarySearch(ans, nums[i])
            ans[idx] = nums[i]
    print(ans)
    return len(ans)


print(lengthOfLISBinarySearchWithout(arr))
