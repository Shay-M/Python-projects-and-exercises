# https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_networkpy103+2020_1/courseware/52a3378d07b4483eb4cdb15b899fd472/89de92924e64477fa43baac6a313e540/?child=first

import socket

# socket.AF_INET: protocol IP
# socket.SOCK_STREAM: protocol TCP
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# my_socket.connect((IP, PORT))
# 127.0.0.1 we use localhost
my_socket.connect(("127.0.0.1", 8820))

data = ""

while data.lower() != "bye":
    msg = input("Please enter your massage:\n")

    #  to Send #encode() convert to binary
    my_socket.send(msg.encode())

    # to Receiver # 1024: number of maximum bytes
    data = my_socket.recv(1024).decode()
    # decode from binary
    print("The server sent: " + data)

my_socket.close()
