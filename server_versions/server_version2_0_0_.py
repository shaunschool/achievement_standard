import socket
import threading
import sign_in as sign_in

HOST = socket.gethostbyname(socket.gethostname())
PORT = 55000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def recieve():
    while True:
        client, address = server.accept()
        print(client)
        print(f"Connected with {str(address)}")
        broadcast(f"{username} joined the server!".encode("ascii"))
        client.send("Connected to the server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f"{client}")

def main():
    # run threads
    pass

if __name__ == "__main__":
    main()