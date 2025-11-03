import socket

from pyexpat.errors import messages


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address =  ("localhost",8080)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Waiting for a connection")

    messages = []

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected by", client_address)

        data = client_socket.recv(1024).decode()
        print(f"Client connected: {data}")

        messages.append(f"Server update: {data}")

        response = f"Server update: {data}"
        client_socket.send('\n'.join(messages).encode())

        client_socket.close()

if __name__ == "__main__":
    server()