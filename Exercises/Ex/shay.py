# import numpy as np

# l, w = (15, 15)
# pixels = np.zeros([l, w])
# x1, y1 = (1, 1)
# x2, y2 = (1, 2)


# if x1 == x2:  # check if not oredenery line.
#     if y1 != y2:  # if not same point
#         pixels[:, x1] = 1
#     else:
#         print("Can't calculate a line with the same point!!!")
# else:  # in case
#     m = ((y2-y1)/(x2-x1))
#     b = y1 - m*x1

#     def line(x): return int(m*x + b)

#     print(f"({y2}-{y1}) / ({x2}-{x1}) = {y2 - y1} /{x2 - x1}  = {m}")

#     print(f"y = {m}x + {b}")
#     for x in range(min(x1, x2), max(x1, x2)+1):
#         y = line(x)
#         print(x, y)
#         pixels[l-y-1][x] = 1

# print(pixels)


# Python3 program to sort an array of
# numbers in range from 1 to n.

# function for sort array
def sortit(arr, n):
    for i in range(n):
        arr[i] = (i+1) * 3


# Driver code
if __name__ == '__main__':
    arr = [15, 12, 9, 6, 3]
    arr = [x//3 for x in arr]
    print(arr)
    n = len(arr)

    # for sort an array
    sortit(arr, n)

    # for print all the element
    # in sorted way
    for i in range(n):
        print(arr[i], end=" ")

# This code is contributed by
# Shrikant13
