import socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    client_socket.connect(server_address)

    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Ответ от сервера: {response}")


    client_socket.close()
if __name__ == "__main__":
    send_message("Привет, сервер!")
    send_message("Как дела?")

