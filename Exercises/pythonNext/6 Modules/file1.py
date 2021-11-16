class GreetingCard:
    def __init__(self, _recipient="Dana Ev", _sender="Eyal Ch"):
        self._recipient = _recipient
        self._sender = _sender

    def greeting_msg(self):
        print(self._sender)
        print(self._recipient)
