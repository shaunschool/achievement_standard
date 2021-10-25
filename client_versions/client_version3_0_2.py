from tkinter import *
import socket
import threading
import sign_in as sign_in
import re
from tkinter import messagebox

global HOST
global PORT
global CLIENT

HOST = "127.0.0.1"
PORT  = 55555

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((HOST, PORT))

global username
username = sign_in.main()
CLIENT.send(username.encode("ascii"))

class GUI:

    messagebox.showwarning("WARNING!", "DISCRETION IS ADVISED WHEN DISCUSSING PRIVATE THINGS ON \"FREE WIFI\", ")

    def __init__(self, parent):

        # background color
        backgroundColor = "#e0e0eb"

        def recieve():
            while True:
                try:
                    message = CLIENT.recv(1024).decode("ascii") + "\n"

                    if re.search(f"^{username}: .", message):
                        pass

                    elif re.search(f"^{username} .", message):
                        insert_foreign_user_message(message)

                    else:
                        message = "\n" + message
                        insert_foreign_user_message(message)
                except:
                    print("An error occured")
                    CLIENT.close()
                    break

        # send button functions
        def insert_local_user_message(message):
            message = f"\nYou: {message}\n"
            self.textDisplay.configure(state=NORMAL)
            self.textDisplay.insert(END, message)
            self.textDisplay.configure(state=DISABLED)
        
        def insert_foreign_user_message(message):
            self.textDisplay.configure(state=NORMAL)
            self.textDisplay.insert(END, message)
            self.textDisplay.configure(state=DISABLED)

        def get_local_user_input():
            message = self.userEntry.get("1.0", END).strip("\n").strip()
            if message == "":
                pass
            else:
                self.userEntry.delete(1.0, END)
                return message

        def send_procedure(message):
            message = f"{message}"
            insert_local_user_message(message)

            message = f"{username}: {message}"
            CLIENT.send(message.encode("ascii"))

        self.topTitleFrame = Frame(parent)
        self.middleTextBoxFrame = Frame(parent)
        self.bottomTextInputFrame = Frame(parent)

         # top title frame setup
        self.topTitleFrame.configure(height=50, width=500, bg=backgroundColor)
        self.topTitleFrame.grid(row=0, column=1)
        self.titleLabel = Label(self.topTitleFrame, text=username, font=("roboto", 20, "bold"), bg=backgroundColor)
        self.titleLabel.place(anchor=CENTER, relx=0.5, rely=0.6)

        # middle text box frame setup
        self.middleTextBoxFrame.configure(height=520, width=500, bg=backgroundColor)
        self.middleTextBoxFrame.grid(row=2, column=1)
        self.textDisplay = Text(self.middleTextBoxFrame, state=DISABLED, cursor="arrow", padx=10, pady=10)
        self.textDisplay.place(relheight=0.96, relwidth=0.968, relx=0.5, rely=0.5, anchor=CENTER)

        # bottom text input frame setup
        self.bottomTextInputFrame.configure(height=130, width=500, bg=backgroundColor)
        self.bottomTextInputFrame.grid(row=3, column=1)

        # text entry space
        self.userEntry = Text(self.bottomTextInputFrame, font=("roboto", 16, "bold"), padx=10, pady=10, wrap="word")
        self.userEntry.place(anchor=W, height=117, relwidth=0.75, rely=0.5, x=8)
        self.userEntry.focus()

        # send button
        self.sendButton = Button(self.bottomTextInputFrame, text="SEND", font=("roboto", 16, "bold"), command=lambda: send_procedure(get_local_user_input()))
        self.sendButton.place(anchor=E, height=117, relwidth=0.2, rely=0.5, x=492)

        recieveThread = threading.Thread(target=recieve)
        recieveThread.start()

def main():
    root = Tk()
    root.title("Chat room")
    root.geometry("500x700")
    root.resizable(height=False, width=False)
    chatRoom = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
