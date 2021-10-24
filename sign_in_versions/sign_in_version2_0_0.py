from tkinter import *

class SignIn:

    def __init__(self, parent):

        # fonts
        headingFont = ("roboto", 21)
        subheadingFont = ("roboto", 13)
        alertMessageFont = ("roboto", 9)

        # background color
        backgroundColor = "#e0e0eb"

        # special characters
        passwordBlackDot = "\u25CF"

        # organisational frames
        self.topFrame = Frame(parent)  # contains "Sign in" heading for widget
        self.middleFrame = Frame(parent)  # contains entry fields for username and password
        self.bottomFrame = Frame(parent)  # contains buttons which capture user inputs




        # ----------------------------- getting input functions -----------------------------

        # get username function
        def get_username():
            username = self.usernameEntry.get()
            return username

        # get password function
        def get_password():
            password = self.passwordEntry.get()
            return password
 
        def details():

            if self.usernameEntry.get().strip() == "":
                self.usernameAlert.configure(text="*username required", fg="red")

            if self.passwordEntry.get().strip() == "":
                self.passwordAlert.configure(text="*password required", fg="red")
            
            if self.usernameEntry.get().strip() != "":
                self.usernameAlert.configure(fg=backgroundColor)

            if self.passwordEntry.get().strip() != "":
                self.passwordAlert.configure(fg=backgroundColor)
            
            if self.usernameEntry.get().strip() != "" and self.passwordEntry.get().strip() != "":
                return get_username(), get_password()




        # ----------------------------- top frame setup -----------------------------

        self.topFrame.configure(width=300, height=50, bg=backgroundColor)
        self.topFrame.grid(row=0, column=0)
        
        self.topFrameText = Label(self.topFrame, bg=backgroundColor, text="Sign in", font=headingFont)
        self.topFrameText.place(anchor=CENTER, relwidth=0.5, relheight=0.8, relx=0.5, rely=0.5)




        # ----------------------------- middle frame setup -----------------------------

        self.middleFrame.configure(width=300, height=250, bg=backgroundColor)
        self.middleFrame.grid(row=1, column=0)
        
        # username label
        self.usernameLabel = Label(self.middleFrame, text="username", font=subheadingFont, bg=backgroundColor)
        self.usernameLabel.place(anchor=NW, x=60, y=40)
        
        # username entry field
        self.usernameEntry = Entry(self.middleFrame, font=subheadingFont)
        self.usernameEntry.place(anchor=NW, x=60, y=70)

        # username entry required alert
        self.usernameAlert =  Label(self.middleFrame, text="", font=alertMessageFont, bg=backgroundColor, fg=backgroundColor)
        self.usernameAlert.place(anchor=NE, x=245, y=95)

        # password label
        self.passwordLabel = Label(self.middleFrame, text="password", font=subheadingFont, bg=backgroundColor)
        self.passwordLabel.place(anchor=NW, x=60, y=120)

        # password entry field
        self.passwordEntry = Entry(self.middleFrame, font=subheadingFont, show=passwordBlackDot)
        self.passwordEntry.place(anchor=NW, x=60, y=150)

        # password entry required alert
        self.passwordAlert =  Label(self.middleFrame, text="", font=alertMessageFont, bg=backgroundColor, fg=backgroundColor)
        self.passwordAlert.place(anchor=NE, x=245, y=175)




        # ----------------------------- bottom frame setup -----------------------------

        self.bottomFrame.configure(width=300, height=50, bg=backgroundColor)
        self.bottomFrame.grid(row=2, column=0)

        # register button
        self.registerButton = Button(self.bottomFrame, text="register", command=details)
        self.registerButton.place(anchor=CENTER, relwidth=0.5, relheight=1, relx=0.25, rely=0.5)

        # sign in button
        self.signInButton = Button(self.bottomFrame, text="sign in", command=details)
        self.signInButton.place(anchor=CENTER, relwidth=0.5, relheight=1, relx=0.75, rely=0.5)


def main():
    root = Tk()
    root.title("Sign in")
    root.geometry("300x350")
    root.resizable(height=False, width=False)
    signInWindow = SignIn(root)
    root.mainloop()

if __name__ == "__main__":
    main()
