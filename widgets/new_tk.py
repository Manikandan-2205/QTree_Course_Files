import tkinter as tk

root  = tk.Tk(className="Sign In")
lab1 = tk.Label(root, text="Email Address:")
lab1.grid(row=0,column=0)
lab2 = tk.Label(root, text="password:")
lab2.grid(row=1,column=0)

bt1 =tk.Button(root,text="Login")
bt1.pack(side = "bottom")
root.mainloop()