# Protocol Constants

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10 ** LENGTH_FIELD_LENGTH - 1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "logout_msg": "LOGOUT",
    "get_question_msg": "GET_QUESTION",
    "send_answer_msg": "SEND_ANSWER",
    "my_score_msg": "MY_SCORE",
    "highscore_msg": "HIGHSCORE"

}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "login_failed_msg": "ERROR"
}  # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
    """
    Gets command name (str) and data field (str) and creates a valid protocol message
    Returns: str, or None if error occured

    build_message('LOGIN', 'aaaa#bbbb')
    "LOGIN       |0009|aaaa#bbbb"
    """

    for pc in PROTOCOL_CLIENT.values():

        # LOGIN      |

        if cmd == pc:
            full_msg = ""
            full_msg += cmd
            # for i in range(CMD_FIELD_LENGTH - len(cmd)):
            #     full_msg += " "

            #  ljust: pad with spaces
            full_msg = full_msg.ljust(CMD_FIELD_LENGTH)
            full_msg += DELIMITER
            break
        else:
            return

    # LOGIN      |0008
    # number_of_length_pad_with_zeros = "0000"
    number_of_length = len(data)
    # number_of_length = len(data.replace(DATA_DELIMITER, ""))
    if 0 <= number_of_length <= 9999:  # ???== LENGTH_FIELD_LENGTH
        number_of_length_pad_with_zeros = (str(number_of_length)
                                           ).zfill(LENGTH_FIELD_LENGTH)
    else:
        return

    full_msg += number_of_length_pad_with_zeros
    full_msg += DELIMITER
    full_msg += data

    return full_msg


def parse_message(data):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None

    parse_message("LOGIN       |0009|aaaa#bbbb")
    ('LOGIN', 'aaaa#bbbb')
    """
    msg_split = data.split(DELIMITER)
    cmd = ""
    if len(msg_split) >= 3:

        for pc in PROTOCOL_CLIENT.values():
            if pc == msg_split[0].strip():
                cmd = pc
                break
            else:
                return None, None

        msg = ""
        if len(str(msg_split[1]).strip().strip("0")) <= LENGTH_FIELD_LENGTH:
            if msg_split[1].strip().isdigit():
                if int(msg_split[1]) == len(msg_split[2]):
                    msg = msg_split[2]
                else:
                    return None, None
            else:
                return None, None
        else:
            return None, None
    else:
        return None, None

    return cmd, msg


def split_data(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None

    split_data("username#password" , 1)
    ['username', 'password']
    """

    msg_split = msg.split(DATA_DELIMITER)
    if len(msg_split) == expected_fields:
        return msg_split
    else:
        return


def join_data(msg_fields):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter.
    Returns: string that looks like cell1#cell2#cell3

    join_data(["username" , "password"])
    'username#password'
    """
    return DATA_DELIMITER.join(str(e) for e in msg_fields)

# print(parse_message("LOGIN   |0009|aaaa#bbbb"))

# build_message("LOGIN", "aaaa#bbbb#bbbb")
