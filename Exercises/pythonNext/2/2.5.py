class Animal:
    def __init__(self, _name, _hunger=0):
        self._name = _name
        self._hunger = _hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger == 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print('_')


class Dog(Animal):
    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal):
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):
    def __init__(self, _name, _hunger=0, _stink_count=6):
        super().__init__(_name, _hunger)

    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')


class Unicorn(Animal):
    def talk(self):
        print('Good day, darling')

    def sing(self):
        print('I’m not your toy...')


class Dragon(Animal):
    def __init__(self, _name, _hunger=0, _color='Green'):
        super().__init__(_name, _hunger)

    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')


def main():
    zoo_lst = []

    Brownie = Dog("Brownie", 10)
    zoo_lst.append(Brownie)

    Zelda = Cat("Zelda", 3)
    zoo_lst.append(Zelda)

    Stinky = Skunk("Stinky", 0)
    zoo_lst.append(Stinky)

    Keith = Unicorn("Keith", 7)
    zoo_lst.append(Keith)

    Lizzy = Dragon("Lizzy", 1450)
    zoo_lst.append(Lizzy)

    for animal in zoo_lst:
        print(type(animal).__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()


main()
