from tkinter import *
import handle_data_file_version1.0.0 as handle_data_file

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




        # ----------------------------- sign in button functions -----------------------------

        def try_sign_in():

            if details() != None:
                username, password = details()

                if handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "correct username and password":
                    successful_sign_in()

                elif handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "incorrect password":
                    incorrect_password()
                
                elif handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "username not found":
                    username_not_found()

            else:
                pass
                
        def incorrect_password():
            self.passwordEntry.delete(0, END)
            print("incorrect password")

        def username_not_found():
            print("username not found")  # try registering

        def successful_sign_in():
            self.usernameEntry.configure(state=DISABLED)
            self.passwordEntry.configure(state=DISABLED)
            self.signInButton.configure(state=DISABLED)
            self.registerButton.configure(state=DISABLED)
            print("signing in")




        # ----------------------------- register button functions -----------------------------
            
        def try_register():

            if details() != None:
                username, password = details()

                if handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "correct username and password":
                    username_already_exists()

                elif handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "incorrect password":
                    username_already_exists()
                
                elif handle_data_file.check_for_match(username, password, handle_data_file.dataSet) == "username not found":
                    successful_register(username, password)

            else:
                pass
        
        def username_already_exists():
            self.usernameEntry.delete(0, END)
            print("username already exists, pick a new one")
        
        def successful_register(username, password):
            handle_data_file.register_user(username, password, handle_data_file.dataSet)
            print("register successful, try signing in!")




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
        self.registerButton = Button(self.bottomFrame, text="register", command=try_register)
        self.registerButton.place(anchor=CENTER, relwidth=0.5, relheight=1, relx=0.25, rely=0.5)

        # sign in button
        self.signInButton = Button(self.bottomFrame, text="sign in", command=try_sign_in)
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