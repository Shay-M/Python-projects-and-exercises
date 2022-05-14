import socket

import chatlib  # To use chatlib functions or consts, use chatlib.****

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678


# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
    """
    Builds a new message using chatlib, wanted code and message.
    Prints debug info, then sends it to the given socket.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: Nothing
    """
    new_message = chatlib.build_message(code, data)
    conn.send(new_message.encode())


def recv_message_and_parse(conn):
    """
    Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occured, will return None, None
    """
    full_msg = conn.recv(1024).decode()
    print("full_msg:", full_msg)

    cmd, data = chatlib.parse_message(full_msg)
    return cmd, data


def connect():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((SERVER_IP, SERVER_PORT))

    return my_socket


def error_and_exit(error_msg):
    print("error_msg:", error_msg)
    quit()


def login(conn):
    username = input("Please enter username: \n")
    password = input("Please enter password: \n")
    # Implement code

    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], username + "#" + password)

    cmd, data = recv_message_and_parse(conn)
    # print(cmd)


def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], "")


def main():
    my_socket = connect()
    login(my_socket)
    # logout(my_socket)


if __name__ == '__main__':
    main()
