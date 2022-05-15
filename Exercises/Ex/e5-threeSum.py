# Given an integer array , return all the triplets
# Notice that the solution set must not contain duplicate triplets.
# https://www.youtube.com/watch?v=jzZsG8n2R9A
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# sort array + loop + loop = O(nlog(n)) + O(n^2) ==  O(n^2)
# from e4 import twoSam
A = [-1, 0, 1, 2, -1, -4]
target = 0


def threeSum(arr, sum):
    result = []  # ask to return list of lists
    arr.sort()  # n log n

    # //? https://realpython.com/python-enumerate/
    for index, currentValue in enumerate(arr):

        if index > 0 and currentValue == arr[index-1]:
            continue

        left, right = index + 1, len(arr) - 1
        while left < right:
            curThreeSum = currentValue + arr[left] + arr[right]

            if (curThreeSum > sum):
                right -= 1
            elif(curThreeSum < sum):
                left += 1
            else:
                result.append([currentValue, arr[left], arr[right]])
                left += 1
                while arr[left] == arr[left-1] and left < right:
                    left += 1

    return result


print('threeSum: ', threeSum(A, target))
