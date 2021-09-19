import socket

server = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 55555))
server.listen()

print(f"HOST: {socket.gethostbyname(socket.gethostname())}")
print("PORT: 55555")

while True:
    client, address = server.accept()
    print(f"Connected to {address}")
    client.send("You are connected".encode())
    client.close()