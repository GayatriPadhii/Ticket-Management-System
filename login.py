# login.py
from tkinter import *
from tkinter import messagebox
import frontend 

USERNAME = "root"
PASSWORD = "Gayatri2002"

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", f"Welcome {user}!")
        root.destroy()
        frontend.launch_gui(user)
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = Tk()
root.title("Login - Movie Ticket System")
root.geometry("400x250")

Label(root, text="Username", font=('Arial', 14)).pack(pady=10)
entry_user = Entry(root, font=('Arial', 14))
entry_user.pack()

Label(root, text="Password", font=('Arial', 14)).pack(pady=10)
entry_pass = Entry(root, show="*", font=('Arial', 14))
entry_pass.pack()

Button(root, text="Login", font=('Arial', 14, 'bold'), command=login).pack(pady=20)

root.mainloop()
