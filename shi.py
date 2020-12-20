from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import ttk


def choice_before_datas():
    global choice_window
    choice_window = Tk()
    choice_window.geometry("1920x1080")
    choice_window.title("HOMEPAGE")
    choice_window.resizable(True, True)

    canvas1 = tk.Canvas(choice_window, width = 400, height = 300,  relief = 'raised')
    canvas1.pack()


    name = Label(choice_window, text="REPORT CARD GENERATION SYSTEM", font=("lucida grande", "40"))
    name.pack()
    # second heading
    s_name = Label(choice_window, text="ARMY PUBLIC SCHOOL", font=("Times", "15"))
    s_name.pack()

    frame = LabelFrame(choice_window, padx=100, pady=50)
    frame.pack()

    stu_btn = Button(frame, text="CLICK HERE!!", bg="RosyBrown1",command=window_for_stu_system)
    stu_btn.pack()

    canvas1.create_window(200, 170, window=stu_btn)

    choice_window.mainloop()
    

def window_for_stu_system():
    global stu
    stu = Tk()
    stu.geometry("550x400")
    stu.title("STUDENT WINDOW")
    # first heading
    name = Label(stu, text="ENTER YOUR DETAILS", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(stu, text="ARMY PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(stu, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Label(frame, text="NAME", padx=20, pady=2)
    delete_record = Label(frame, text="CLASS", padx=20, pady=2)
    update_record = Label(frame, text="ROLL NO", padx=11, pady=2)
    showall_record = Label(frame, text="FATHER s NAME", padx=11, pady=2)
    stu_table = Button(frame, text="SUBMIT", padx=2, pady=2 , command = window_for_stu_system1)

    name = Entry(frame , bd = 5)
    class_sec = Entry(frame , bd = 5)
    rollno = Entry(frame , bd = 5)
    fname = Entry(frame , bd = 5)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=1, column=0, padx=15, pady=9)
    update_record.grid(row=2, column=0, pady=9, padx=30)
    showall_record.grid(row=3, column=0, padx=15, pady=9)
    stu_table.grid(row=5, column=0, padx=30)

    name.grid(row=0 , column=1)
    class_sec.grid(row=1 , column=1)
    rollno.grid(row=2 , column=1)
    fname.grid(row=3 , column=1)

    stu.mainloop()

def window_for_stu_system1():
    global stu1
    stu1 = Tk()
    stu1.geometry("1920x1080")
    stu1.title("MARKS")
    # first heading
    name = Label(stu1, text="ENTER YOUR MARKS", font=("lucida grande", "25"), anchor="center")
    name.pack()
    # second heading
    s_name = Label(stu1, text="ARMY PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.pack()
    
    frame1 = LabelFrame(stu1, padx=50, pady=50)
    frame1.grid(row=3, column=0)
 
    add_record1 = Label(frame1, text="ENGLISH", padx=20, pady=2)
    delete_record1 = Label(frame1, text="CHEMISTRY", padx=20, pady=2)
    update_record1 = Label(frame1, text="MATHS", padx=11, pady=2)
    showall_record1 = Label(frame1, text="PHYSICS", padx=11, pady=2)
    showsome_record1 = Label(frame1, text="COMPUTER SCIENCE", padx=11, pady=2)
    stu_table1 = Button(frame1, text="SUBMIT", padx=2, pady=2 , command = calltext)

    add_record1.grid(row=0, column=0, padx=30, pady=9)
    delete_record1.grid(row=1, column=0, padx=15, pady=9)
    update_record1.grid(row=2, column=0, pady=9, padx=30)
    showall_record1.grid(row=3, column=0, padx=15, pady=9)
    showsome_record1.grid(row=4, column=0, padx=15, pady=9)
    stu_table1.grid(row=5, column=0, padx=30)

    name = Entry(frame1 , bd = 5)
    class_sec = Entry(frame1 , bd = 5)
    rollno = Entry(frame1 , bd = 5)
    fname = Entry(frame1 , bd = 5)
    cs = Entry(frame1 , bd = 5)

   

    name.grid(row=0 , column=1)
    class_sec.grid(row=1 , column=1)
    rollno.grid(row=2 , column=1)
    fname.grid(row=3 , column=1)
    cs.grid(row = 4 , column = 1)
    
    stu1.mainloop()


def database_start():
    global root
    root = Tk()
    root.geometry("1920x1080")
    root.title("LIBRARY WINDOW")
    # first heading
    name = Label(root, text="REPORT CARD MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(root, text="ARMY PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(root, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Button(frame, text="Add record", padx=20, pady=2,command = database_add)
    delete_record = Button(frame, text="Delete record", padx=20, pady=2,command=submit_delete)
    update_record = Button(frame, text="Update record", padx=11, pady=2,command= submit_update)
    showall_record = Button(frame, text="Show All record", padx=11, pady=2,command=show_all_submit)
    showone_record = Button(frame, text="Show One record", padx=7, pady=2,command=show_one_rec)
    Lib_table = Button(frame, text="Create Lib table", padx=11, pady=2, command=create_table)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=0, column=1, padx=15, pady=9)
    update_record.grid(row=1, column=0, pady=9, padx=30)
    showall_record.grid(row=1, column=1, padx=15, pady=9)
    showone_record.grid(row=2, column=0, pady=9)
    Lib_table.grid(row=2, column=1, padx=30)

    root.mainloop()


def login_info():
    global login_screen
    global root
    global user_entry
    global password_entry
    global main
    global login_screen

    username1 = user_entry.get()
    password1 = password_entry.get()

    user_entry.delete(0,END)
    password_entry.delete(0,END)

    list_of_files = os.listdir()
    if username1+".txt" in list_of_files:
        file = open(username1+".txt", "r")
        verify1 = file.readline()
        verify2 = file.readline()

        if password1 == verify2:
            messagebox.showinfo("Done", "Login Successfull")
            main.withdraw()
            login_screen.withdraw()
            choice_before_datas()

        else :
            messagebox.showerror("Error","Wrong Password!!!!")
            login_screen.destroy()

    else:
       messagebox.showerror("Not found", "USER NOT FOUND!!!!")
       login_screen.destroy()


def login():
    global login_screen
    global username
    global password
    global user_entry
    global password_entry
    global main
    # global user_verify
    # global password_verify

    login_screen = Toplevel(main)
    login_screen.title("LOGIN")
    login_screen.geometry("300x400")


    # user_verify = StringVar
    # password_verify = StringVar

    Label(login_screen, text="Enter your Login info. below:-", font=("lucida grande", "17")).grid()
    Label(login_screen, text="Username-", font=("lucida grande", "10")).grid()
    user_entry = Entry(login_screen, borderwidth=2)
    user_entry.grid()

    Label(login_screen, text=" ").grid()

    Label(login_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(login_screen,borderwidth=2)
    password_entry.grid()

    Label(login_screen, text=" ").grid()

    login = Button(login_screen,text="Login",padx=10,command= login_info)
    login.grid()


def register_info():
    global username
    global password
    global user_entry
    global password_entry

    user_info = user_entry.get()
    password_info = password_entry.get()

    file = open(user_info+".txt","w")
    file.write(user_info+"\n")
    file.write(password_info)

    user_entry.delete(0,END)
    password_entry.delete(0, END)

    messagebox.showinfo("Succesfull","Registry successful")

def register():
    global username
    global password
    global user_entry
    global password_entry

    register_screen = Toplevel(main)
    register_screen.title("REGISTER HERE")
    register_screen.geometry("300x400")
    username = StringVar
    password = StringVar
    Label(register_screen,text="Enter your details below :-",font=("lucida grande","19")).grid()

    Label(register_screen, text="Username-", font=("lucida grande","10")).grid()
    user_entry = Entry(register_screen,textvariable = username,borderwidth = 2)
    user_entry.grid()



    Label(register_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(register_screen, textvariable=password,borderwidth = 2)
    password_entry.grid()

    register_in = Button(register_screen,text ="Register Info",command =register_info)

    register_in.grid()


    register_screen.mainloop()


def main_screen():
    global main
    main = Tk()
    main.title("LIBRARY MANAGEMENT SYSTEM")
    main.geometry("300x400")
    main.configure(background="misty rose")
    heading_main = Label(main, text= "LOGIN",  font=("Helvetica","40"),anchor="center",bg= "misty rose",padx=10)
    heading_main.grid(row=0,column=0,padx= 65)

    login_button = Button(main, text="LOGIN", padx=40, pady=3,command = login)
    login_button.grid(pady = 25)

    register_button =Button(main,text= "REGISTER",padx= 35, pady=3, command= register)
    register_button.grid(pady = 15)

    exit_button = Button(main, text="EXIT", padx=45, pady=3, command=quit_main)
    exit_button.grid(pady = 25)

    main.mainloop()

def quit_main():
    global main
    main.destroy()


main_screen()
