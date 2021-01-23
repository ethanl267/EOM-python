from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk


root = tk.Tk()
root.title("Admin")
root.geometry('400x300')
root.configure(background='grey')


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='lifechoicesOnline',
                               host='127.0.0.1', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

#Code
def create_user():

    # names = fullname.get()
    user_name = username.get()
    pass_word = password.get()
    # phone_number = number.get()
    # usertbl = "INSERT INTO Admin VALUES (%s, %s, %s, %s)"
    # mycursor.execute(usertbl, [names, user_name, pass_word, phone_number])
    # mydb.commit()
    #
    # messagebox.showinfo("message", "Admin user recognized.")
    usebtn="SELECT * FROM Admin where Username = %s and Password = %s"
    mycursor.execute(usebtn, [ (user_name), (pass_word)])
    results=mycursor.fetchall()

    if results:


        table = Tk()
        table.title("Database tables")
        table.geometry("1100x500")
        table.resizable(False, False)

        # SHOWING USERS IN A LIST BOX

        fname = Label(table, text="Full name")
        usernm = Label(table, text="Username")
        stat = Label(table, text="Status")

        fnamemList = Listbox(table, width=25)
        usernmList = Listbox(table, width=25)
        statList = Listbox(table, width=25)

        # SHOWING SIGN IN/SIGN OUT TIMES IN A LIST BOX
        Username = Label(table, text="Username")
        signin = Label(table, text="Sign in")
        signout = Label(table, text="Sign out")

        usernamelist = Listbox(table, width=25)
        inlist = Listbox(table, width=25)
        outlist = Listbox(table, width=25)

        # FOR LOOPS (USERS LIST BOX)
        mycursor.execute("SELECT * FROM Admin")
        tab = mycursor.fetchall()

        for i in tab:
            fnamemList.insert(END, i)

        mycursor.execute("SELECT * from Admin")
        tab = mycursor.fetchall()

        for i in tab:
            usernmList.insert(END, i)

        mycursor.execute("SELECT * from Admin")
        tab = mycursor.fetchall()

        for i in tab:
            statList.insert(END, i)

        # # FOR LOOPS FOR TIME REGISTER
        # mycursor.execute("SELECT username from sign_register")
        # tab = mycursor.fetchall()
        #
        # for i in tab:
        # usernamelist.insert(END, i)

        mycursor.execute("SELECT sign_in from register_time")
        tab = mycursor.fetchall()

        for i in tab:
            inlist.insert(END, i)

        mycursor.execute("SELECT sign_out from register_time")
        tab = mycursor.fetchall()

        for i in tab:
            outlist.insert(END, i)

        fname.place(x=5, y=4)
        fnamemList.place(x=5, y=20)
        usernm.place(x=225, y=4)
        usernmList.place(x=225, y=20)
        stat.place(x=445, y=4)
        statList.place(x=445, y=20)

        # Username.place(x=445, y=4)
        # usernamelist.place(x=445, y=220)
        signin.place(x=665, y=4)
        inlist.place(x=665, y=20)
        signout.place(x=885, y=4)
        outlist.place(x=885, y=20)

        table.mainloop()
    else:
        messagebox.showinfo('Error', 'Incorrect Password/Username')
        quit()


    # except ValueError as i:
    #     print(i)
    #     messagebox.showinfo("ERROR", 'You are already signed in.')





# entries

username = Entry(root, width=35)
username.place(x=80, y=60)

password = Entry(root, width=35, show="*")
password.place(x=80, y=90)


label = Label(root, text='username')
label.place(x=10, y=60)

label = Label(root, text='password')
label.place(x=10, y=90)




# button
btn1 = Button(root, text='Create Admin user', bg='black', fg='white',command=create_user)
btn1.place(x=100, y=150)
btn1 = Button(root, text='Exit', bg='black', fg='white',command=exit)
btn1.place(x=250, y=150)





root.mainloop()
