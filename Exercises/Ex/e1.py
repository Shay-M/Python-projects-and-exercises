import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


def bres(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    print('x = %s, y = %s' % (x, y))
    # initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bres(x1, y1, x2, y2)


if __name__ == "__main__":
    main()


# ----------------------------------------------------------------

# import numpy as np

# l, w = (5, 10)
# pixels = np.zeros([l, w])
# pixels = [0] * w
# x1, y1 = (1, 1)
# x2, y2 = (1, 1)


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

# pixels


def bresenham(x1, y1, x2, y2):

    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2+1):

        print("(", x, ",", y, ")\n")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y+1
            slope_error_new = slope_error_new - 2 * (x2 - x1)


# driver function
if __name__ == '__main__':
    x1 = -3
    y1 = 2
    x2 = 15
    y2 = 5
    bresenham(x1, y1, x2, y2)
