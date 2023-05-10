import socket

# from src import client

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 445
# client_socket.connect((host, port))


def register_middleware(authenticate_client):
    return register_middleware(authenticate_client)
