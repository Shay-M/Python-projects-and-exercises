import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, _recipient="Dana Ev", _sender="Eyal Ch", _sender_age=0):
        super().__init__(_recipient, _sender)
        self._sender_age = _sender_age

    def greeting_msg(self):
        super()
        print("Happy birthday")
        print(self._sender_age)
