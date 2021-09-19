import socket
import threading

nickname = input("chose nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.112.208", 55555))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "LOGIN":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode("ascii"))

def main():
    recieveThread = threading.Thread(target=recieve)
    writeThread = threading.Thread(target=write)

    recieveThread.start()
    writeThread.start()

if __name__ == "__main__":
    main()