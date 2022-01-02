# https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_networkpy103+2020_1/courseware/52a3378d07b4483eb4cdb15b899fd472/e3da5aa2ac79413cbdced241bdc32c18/?child=first

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 0.0.0.0: listen to all who are connected to outside ip or to Local Host
server_socket.bind(("0.0.0.0", 8820))

server_socket.listen()
print("Server is up and running")

# wait for client connect
(client_socket, client_address) = server_socket.accept()

print("Client connected!")
data = ""
while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)

    if data.lower() == "bye":
        data = " "
    if data.lower() == "quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    client_socket.send(data.encode())

# close client_socket after finish
client_socket.close()

# wait for more client connect? or close
server_socket.close()
