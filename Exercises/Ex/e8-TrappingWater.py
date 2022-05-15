# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is
# represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
#  6 units of rain water (blue section) are being trapped.

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
# height = [4, 2, 0, 3, 2, 5]  # 9
# height = [1, 0, 0, 2]  # 2


def trap(height):

    n = len(height)
    highest = 0
    lefthighest = []
    righthighest = []
    result = 0

    for i in range(n):
        lefthighest.append(highest)
        highest = max(highest, height[i])
    highest = 0
    print(lefthighest)

    for i in range(n-1, -1, -1):
        righthighest.append(highest)
        highest = max(highest, height[i])
    righthighest = righthighest[::-1]
    print(righthighest)

    for i in range(n):
        h = min(lefthighest[i], righthighest[i])

        if h > height[i]:
            result += h-height[i]
    return result


# print(">> ", trap(height))


# ----------------------------------------------------------------
# https://www.youtube.com/watch?v=ZI2z5pq0TqA

def trap2(height):
    l, r = 0, len(height) - 1

    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

    while l <= r:
        if height[l] < height[r]:
            if maxleft > height[l]:
                res += (maxleft-height[l])
            else:
                maxleft = height[l]
            l += 1
        else:
            if maxright > height[r]:
                res += (maxright-height[r])
            else:
                maxright = height[r]
            r -= 1
    return res


print(">> ", trap2(height))
