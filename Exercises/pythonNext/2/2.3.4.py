class Pixel:

    def __init__(self, _x, _y, _red=0, _green=0, _blue=0):
        self._red = _red
        self._green = _green
        self._blue = _blue
        self._x = _x
        self._y = _y

    def set_coords(self, _x, _y):
        self._x = _x
        self._y = _y

    def set_grayscale(self):
        average = int((self._red + self._green + self._blue) / 3)
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):  # X: 5, Y: 6, Color: (0, 55, 78)
        color_name = ''
        if self._red == 0 and self._green == 0:
            color_name = 'Blue'
        elif self._red == 0 and self._blue == 0:
            color_name = 'Green'
        elif self._green == 0 and self._blue == 0:
            color_name = 'Red'

        # int((self._red + self._green + self._blue))
        print(f'X: {self._x} ,Y: {self._y},Color: ({self._red},{self._green},{self._blue}) {color_name}')


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


main()
