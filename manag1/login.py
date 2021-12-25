from tkinter import *
import sqlite3
import tkinter
from tkinter.ttk import Separator
from tkinter import messagebox


conn = sqlite3.connect('mydb.db')
c = conn.cursor()
ws = Tk()
ws.title('Gestion de cabinet médical')
ws.config(bg='#0B5A81')
ws.geometry('600x450')

f = ('Times', 14)
img = PhotoImage(file= "momo.png" ) 
label = Label(ws, image=img)
label.place(x = 240,y = 50) 
left_frame = Frame(
    ws,
    bd=2,
    bg='#B5C9E2',  
    relief=SOLID,
    padx=20,
    pady=10,

    )

Label(
    left_frame,
    text="Username :",
    bg='#B5C9E2',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Password :",
    bg='#B5C9E2',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame,
    font=f
    )
pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
    )

def login_verifier():
    for row in c.execute("Select * from login"):
            username = row[0]
            pwd = row[1]
       
   

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username ne peut pas être vide"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password ne peut pas être vide"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
              
              ws.destroy()            
              import general
       
        else:
            messagebox.showerror('Gestion de cabinet médical', 'Username ou Passoword invalide')
    else:
        messagebox.showerror('', warn)
login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=login_verifier
    )

email_tf.grid(row=0, column=1, pady=20, padx=30)
pwd_tf.grid(row=1, column=1, pady=20, padx=30)
login_btn.grid(row=2, column=1, pady=20, padx=20)
left_frame.pack(side= BOTTOM, pady=20)

ws.iconbitmap(r'logo.ico')
ws.mainloop()