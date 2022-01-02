import random
import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 8820))

server_socket.listen()
print("Server is up and running")

# wait for client connect
(client_socket, client_address) = server_socket.accept()

print("Client connected!")
data = ""
while True:

    data = client_socket.recv(1024).decode()
    print("" + data)
    if data == "NAME":
        client_socket.send("101_ling".encode())
    elif data == "TIME":
        localtime = time.asctime(time.localtime(time.time()))
        client_socket.send(localtime.encode())
    elif data == "RAND":
        random_number = str(int(random.random() * 10))
        client_socket.send(random_number.encode())
    elif data.lower() == "bye":
        data = " "
    elif data.lower() == "quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    else:
        client_socket.send("try again!\n".encode())

# close client_socket after finish
client_socket.close()

# wait for more client connect? or close
server_socket.close()
