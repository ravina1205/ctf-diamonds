from tkinter import *

root = Tk()

username = "punam madam" #that's the given username
password = "12345" #that's the given password

#username entry
username_entry = Entry(root)
username_entry.pack()


password_entry = Entry(root, show='*')
password_entry.pack()

def trylogin():
    if username == username_entry.get() and password == password_entry.get():
        print("Correct")
    else:
        print("Wrong")


button = Button(root, text="check", command = trylogin)
button.pack()


root.mainloop()



# from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
#
# username = ("<script>")
# password = ("")
#
#
# def try_login():
#     print("Trying to login...")
#     if username_guess.get() == username:
#         messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
#     else:
#         messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
#
# #Gui Things
# window = Tk()
# window.resizable(width=FALSE, height=FALSE)
# window.title("Log-In")
# window.geometry("200x150")
#
# #Creating the username & password entry boxes
# username_text = Label(window, text="Username:")
# username_guess = Entry(window)
# password_text = Label(window, text="Password:")
# password_guess = Entry(window, show="*")
#
# #attempt to login button
# attempt_login = Button(text="Login", command=try_login)
#
# username_text.pack()
# username_guess.pack()
# password_text.pack()
# password_guess.pack()
# attempt_login.pack()
# #Main Starter
# window.mainloop()