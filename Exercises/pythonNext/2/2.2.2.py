class Dog:
    count_animals = 0

    def __init__(self, age, name="no name"):
        self._name = name
        self._age = age
        Dog.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name


def main():
    ling = Dog(14, "ling")
    milky = Dog(54)

    ling.birthday()

    print(ling.get_age())
    print(milky.get_age())

    print(ling.get_name())
    print(milky.get_name())

    milky.set_name("boly")
    print(milky.get_name())

    print(Dog.count_animals)


main()
