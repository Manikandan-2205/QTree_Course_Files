from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title("Sign In")
root.geometry("250x100")
username_label = Label(root, text="Email Address:")
username_label.pack()

username_entry = Entry(root,show="Enter Your Vaild MailID")
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

login = tk.Button("Login").pack()

root.mainloop()