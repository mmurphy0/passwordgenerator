import tkinter as tk
from tkinter import messagebox

def add_pwd():
    while True:
        try:
            label = label_entry.get()
            usr = usr_entry.get()
            pwd = str(pwd_entry.get())

            with open('Passwords.txt','a') as file:
                file.write(label + '\n' + 'Username ' + usr + '\n' + 'Password ' + pwd + '\n' + '----------' + '\n')

            messagebox.showinfo('Confirmation','Password successfully saved')
            
            break
        except ValueError:
            messagebox.showinfo('Error','Please make sure all text boxes have been used')
            continue

root = tk.Tk()
root.title('Add New Password')
root.geometry('280x115')
root.minsize(280,115)
root.maxsize(280,115)

label_label = tk.Label(
    root,
    text='Label:',
    font=('Arial',15)
)
label_label.grid(
    row=1,
    column=1
)

label_entry = tk.Entry(root)
label_entry.grid(
    row=1,
    column=2
)

usr_label = tk.Label(
    root,
    text='Username',
    font=('Arial',15)
)
usr_label.grid(
    row=2,
    column=1
)

usr_entry = tk.Entry(root)
usr_entry.grid(
    row=2,
    column=2
)

pwd_label = tk.Label(
    root,
    text='Password',
    font=('Arial',15)
)
pwd_label.grid(
    row=3,
    column=1
)

pwd_entry = tk.Entry(root)
pwd_entry.grid(
    row=3,
    column=2
)

submit_btn = tk.Button(
    root,
    text='Add Password',
    width=30,
    font=('Arial'),
    command=add_pwd
)
submit_btn.grid(
    row=4,
    column=1,
    columnspan=2
)

root.mainloop()