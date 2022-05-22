# https://www.youtube.com/watch?v=RGB-wlatStc
# https://github.com/daQuincy/Bresenham-Algorithm/blob/master/bresenham.py
# not work her
# import matplotlib.pyplot as plt

# plt.title("Bresenham Algorithm")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")


# def bres(x1, y1, x2, y2):
#     x, y = x1, y1
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     gradient = dy/float(dx)

#     if gradient > 1:
#         dx, dy = dy, dx
#         x, y = y, x
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2

#     p = 2 * dy - dx
#     print('x = %s, y = %s' % (x, y))
#     # initialize the plotting points
#     xcoordinates = [x]
#     ycoordinates = [y]

#     for k in range(dx):
#         if p > 0:
#             y = y + 1 if y < y2 else y - 1
#             p = p + 2 * (dy - dx)
#         else:
#             p = p + 2 * dy

#         x = x + 1 if x < x2 else x - 1

#         print('x = %s, y = %s' % (x, y))
#         xcoordinates.append(x)
#         ycoordinates.append(y)

#     plt.plot(xcoordinates, ycoordinates)
#     plt.show()


# def main():
#     x1 = int(input("Enter the starting point of x: "))
#     y1 = int(input("Enter the starting point of y: "))
#     x2 = int(input("Enter the end point of x: "))
#     y2 = int(input("Enter the end point of y: "))

#     bres(x1, y1, x2, y2)


# if __name__ == "__main__":
#     main()


# ----------------------------------------------------------------


def bresenham(x1, y1, x2, y2, arr):
    dy = abs(y2 - y1)
    dx = x2 - x1

    if dx < 0:
        x, y = x1, y1
        x1, y1 = x2, y2
        x2, y2 = x, y
        dx = abs(dx)

    m_new = 2 * (dy)  # pk < 0
    slope_error_new = m_new - (dx)  # pk > 0

    y = y1

    for x in range(x1, x2 + 1):

        # print("(", x, ",", y, ")")
        arr[x][y] = 1

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (dx)

    print(arr)


# driver function
if __name__ == '__main__':

    x1 = 8
    y1 = 6
    x2 = 1
    y2 = 1

    l, w = (10, 10)

    import numpy as np

    pixels = np.zeros([l, w]).astype(int)

    bresenham(x1, y1, x2, y2, pixels)
    print()
    bresenham(x2, y2, x1, y1, pixels)
