from  tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from datetime import *

root=tk.Tk()
root.title("Login page")
root.geometry('450x400')
root.configure(background='grey')


def reg():
    if btn2:
        root.withdraw()
        import register
        register




#code
mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',database='lifechoicesOnline',host='127.0.0.1',auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

def verify():
        user_verification=username.get()
        pass_verification=password.get()
        sql="Select * from User where username = %s and password =%s"
        mycursor.execute(sql, [(user_verification), (pass_verification)])
        results=mycursor.fetchall()
        if results:
            messagebox.showinfo('Message', 'Logged in successfully')

            root = Tk()
            root.title("Sign-in Sign-out")
            root.geometry("250x100")
            signIn = datetime.now()
            x = signIn.strftime("%H:%M:%S")

            def sign_out():
                timeout = datetime.now()
                y = timeout.strftime("%H:%M:%S")
                z = username.get()
                infotime = z,x, y
                timeComm = 'INSERT INTO register_time (Username, sign_in , sign_out) VALUES(%s,%s,%s)'

                mycursor.execute(timeComm, infotime)
                mydb.commit()
                messagebox.showinfo('Message', 'Signed out!')
                root.destroy()

            # button
            btn3 = Button(root, text='sign-out', bg='black', fg='white', command=sign_out)
            btn3.place(x=10, y=10)

         # for i in results:
         #        logged()
         #        break
        else:
            failed()


def logged():
    messagebox.showinfo('you have logged in')

def failed():
    messagebox.showinfo('wrong login')



#labels
label=Label(root, text='username')
label.place(x=10, y=30)

label=Label(root, text='password')
label.place(x=10, y=60)

#entries
username=Entry(root, width=20)
username.place(x=80 , y=30)

password=Entry(root, width=20)
password.place(x=80 , y=60)

def quit():
    y=messagebox.askquestion("Exit application",'Are you sure you want to exit?')
    if y == 'yes':
        root.destroy()
    else:
        pass


#button
btn1=Button(root, text='login', bg='blue',command=verify)
btn1.place(x=20,y=90)
btn2=Button(root, text='register',bg='black',fg='white',command=reg)
btn2.place(x=90, y=90)
btn3=Button(root, text='Quit',bg='red',command=quit)
btn3.place(x=170, y=90)

def hotkey():
    import admin
    admin

root.bind("<Control-a>", lambda x: hotkey())

#design login



root.mainloop()
