import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, _username):
        self._username = _username

    def __str__(self):
        return "%s Contains invalid characters!" % self._username


class UsernameTooShort(Exception):

    def __str__(self):
        return "User name Too Short!"


def check_input(username, password):
    OK = 'Ok'
    if 16 > len(username) > 3:
        for i in username:
            if i not in (string.ascii_letters or string.digits or i == '_'):
                raise UsernameContainsIllegalCharacter(username)
        print(OK)


# print(string.ascii_lowercase)
#
# print(string.ascii_letters)
# print(string.digits)
check_input("username", "password")
