class BigThing:
    def __init__(self, _same_value):
        self._same_value = _same_value

    def size(self):
        if isinstance(self._same_value, int):
            return self._same_value
        elif isinstance(self._same_value, str or list or dict):
            return len(self._same_value)


class BigCat(BigThing):
    def __init__(self, _same_value, _weight):
        # super().__init__(_same_value)
        self._weight = _weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "Ok"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())

    cutie = BigCat("mitzy", 22)
    print(cutie.size())


main()
