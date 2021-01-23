from  tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from datetime import

root=tk.Tk()
root.title("Sign-in and Sign-out")
root.geometry('350x300')

#code
mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',database='lifechoicesOnline',host='127.0.0.1',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

def sign_out():
    timeout = datetime.now()
    x= timeout.strftime("%H:%M:%S")
    y = label.get()
    infotime= x, y
    timeComm = 'INSERT INTO time_register (Username, sign_in , sign_out) VALUES(%s,%s,%s)'

    mycursor.execute(timeComm,infotime)
    mydb.comit()
    messagebox.showinfo('Message', 'Signed out!')
    root.destroy()





#button
btn3=Button(root,text='sign-out',bg='black', fg='white',command=sign_out)
btn3.place(x=50,y=100)

root.mainloop()