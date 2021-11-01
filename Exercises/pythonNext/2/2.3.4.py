class Pixel:

    def __init__(self, _x, _y, _red=0, _green=0, _blue=0):
        self._red = _red
        self._green = _green
        self._blue = _blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y
