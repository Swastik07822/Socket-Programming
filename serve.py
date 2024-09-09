import socket
import threading

# Server setup
host = '127.0.0.1'  # Localhost
port = 12345        # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

clients = []
nicknames = []

# Broadcast messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle individual client connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Accept incoming client connections
def receive_connections():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is listening...")
receive_connections()
