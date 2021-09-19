import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = index.clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode("ascii"))
            nicknames.remove(nicknames)
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nicknames)
        clients.append(client)

        print(f"Nickname of client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode("ascii"))
        client.send("Connected to the server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("\n --------------------------------")
print(" [STARTING] Server is starting...\n")
print(f" HOST = {socket.gethostbyname(socket.gethostname())}")
print(f" PORT = {port}")
print(" --------------------------------")

recieve()