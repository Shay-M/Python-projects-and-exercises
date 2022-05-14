# TWO SUM II: 1-indexed array of integers numbers that is already **sorted** in non-decreasing order,
# find two numbers such that they add up to a specific target number.

# Input: numbers = [1, 3 ,4, 5, 7, 10, 11], target = 9
# Output: [1,2] * ask for index start with 1 not 0

A = [1, 3, 4, 5, 7, 10, 11]
target = 9


def twoSam(arr, sum):
    left, right = 0, len(arr) - 1

    while left < right:
        curSum = arr[left] + arr[right]

        if (curSum > sum):
            right -= 1
        elif(curSum < sum):
            left += 1
        else:
            return [left + 1, right + 1]

    return []


# print('twoSam: ', twoSam(A, target))
