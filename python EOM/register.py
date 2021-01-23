from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

# from EOM import mycursor

root = tk.Tk()
root.title("Register")
root.geometry('400x300')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='lifechoicesOnline',
                               host='127.0.0.1', auth_plugin='mysql_native_password')


mycursor=mydb.cursor()
# code
def enter():
    try:
        names = fullname.get()
        user_name=username.get()
        pass_word=password.get()
        phone_number=number.get()
        usertbl = "INSERT INTO User VALUES (%s, %s, %s, %s)"
        mycursor.execute(usertbl, [names, user_name, pass_word, phone_number])
        mydb.commit()
        messagebox.showinfo("message","sucessfully regsitered")
    except ValueError as i:
        print(i)
        messagebox.showinfo("ERROR",'This already exists')



# entries
fullname = Entry(root, width=35)
fullname.place(x=80, y=30)

username = Entry(root, width=35)
username.place(x=80, y=60)

password = Entry(root, width=35, show="*")
password.place(x=80, y=90)

number = Entry(root, width=35)
number.place(x=80, y=120)

# labels
label = Label(root, text='full name')
label.place(x=10, y=30)

label = Label(root, text='username')
label.place(x=10, y=60)

label = Label(root, text='password')
label.place(x=10, y=90)

label = Label(root, text='phone.no')
label.place(x=10, y=120)

# button
btn1 = Button(root, text='register', bg='red', command=enter)
btn1.place(x=100, y=150)
btn2 = Button(root, text='Exit', bg='red', command=exit)
btn2.place(x=170, y=150)



root.mainloop()
