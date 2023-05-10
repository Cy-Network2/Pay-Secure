import socket

# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get server hostname
host = socket.gethostname()

# bind socket to a port
port = 12345
server_socket.bind((host, port))

# listen for incoming connections
server_socket.listen(1)

print('Server is running on {}:{}'.format(host, port))

while True:
    # accept incoming connection
    client_socket, address = server_socket.accept()

    # read incoming message from client
    message = client_socket.recv(1024).decode()

    # print message and address of client
    print('Received message from {}: {}'.format(address, message))

    # send message to other clients
    client_socket.send('Received: {}'.format(message).encode())

    # close connection to client
    client_socket.close()


def encrypt_data(data, hashes):
    pass
