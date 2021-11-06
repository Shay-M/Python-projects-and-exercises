class UnderAge(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "you under age 18, wait %s year" % str(18 - self._arg)

    def get_arg(self):
        return self._arg


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation("ling", 3)


main()
