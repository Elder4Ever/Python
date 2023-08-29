import os
import string
import json
import random
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from  tkinter import ttk
import sqlite3
from sqlite3 import Error

filename = 'C:/Users/Brandon/Desktop/Python/Basic Gui/settings.json'
title = "Brandon's Password Generator"
version = "Version: Dev-Alpha-1.0"
lic = "This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license."

def about_screen():
    def about_on_closing():
        root.deiconify()
        about.destroy()
    root.withdraw()
    about = Tk()
    about.resizable(False,False)
    about.geometry('400x300')
    about.title("About")

    w = Label(about, text=title,font=("Arial", 18))
    w.pack()

    ver = Label(about, text=version, font=("Arial", 12))
    ver.pack()

    license = Label(about, text=lic, font=("Arial", 10), wraplength=350, justify="center")
    license.pack(padx=20, pady=40)
    about.protocol("WM_DELETE_WINDOW",about_on_closing)
    about.mainloop()

def local_data_screen():
    data_screen = Tk()
    data_screen['bg'] = 'white'
    data_screen.geometry("500x500")
    data_screen.title('Password Database')

    table_frame = Frame(data_screen)
    table_frame.pack()

    datatable = ttk.Treeview(table_frame)

    datatable['columns'] = ('account_id', 'user_email', 'password', 'name', 'url', 'created_date')

    datatable.column("#0", width=0,  stretch=NO)
    datatable.column("account_id",anchor=CENTER, width=80)
    datatable.column("user_email",anchor=CENTER,width=80)
    datatable.column("password",anchor=CENTER,width=80)
    datatable.column("name",anchor=CENTER,width=80)
    datatable.column("url",anchor=CENTER,width=80)
    datatable.column("created_date",anchor=CENTER,width=80)

    datatable.heading("#0",text="",anchor=CENTER)
    datatable.heading("account_id",text="Account ID",anchor=CENTER)
    datatable.heading("user_email",text="Email",anchor=CENTER)
    datatable.heading("password",text="Password",anchor=CENTER)
    datatable.heading("name",text="Name",anchor=CENTER)
    datatable.heading("url",text="Url",anchor=CENTER)
    datatable.heading("created_date",text="Account Saved Date",anchor=CENTER)

    datatable.insert(parent='',index='end',iid=0,text='', values=('1','Ninja','101','Oklahoma', 'Moore','08/28/23'))

    datatable.pack()

    data_screen.mainloop()

def settings():
    if os.path.exists(filename):
        
        root.withdraw()

        def settings_on_closing():
            root.deiconify()
            settings.destroy() 

        def save_settings():
            f = open(filename,'r+')
            data = json.load(f)
            data['settings']['encrypted'] = False
            data['settings']['count'] = 0
            data['settings']['lowercase'] = val1.get()
            data['settings']['uppercase'] = val2.get()
            data['settings']['numbers'] = val3.get()
            data['settings']['special'] = val4.get()
            f.seek(0)
            f.truncate()
            f.write(json.dumps(data))
            savedLabel.configure(text="Saved")
        
        settings = Toplevel()
        settings.resizable(False,False)
        settings.geometry('500x300')
        settings.title("Settings")

        global lowerbox
        global upperbox
        global numberbox
        global specialbox
        global Strength
        Strength = []

        f = open(filename,'r+')
        data = json.load(f)
        lower = data['settings']['lowercase']
        upper = data['settings']['uppercase']
        num = data['settings']['numbers']
        spec = data['settings']['special']
        
        if lower == 1:
            val1 = IntVar(value=1)
            lowerbox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            Strength = Strength + lowerbox
        else:
            val1 = IntVar(value=0)

        if upper == 1:
            val2 = IntVar(value=1)
            upperbox = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            Strength = Strength + upperbox
        else:
            val2 = IntVar(value=0)

        if num == 1:
            val3 = IntVar(value=1)
            numberbox = ['1','2','3','4','5','6','7','8','9','0']
            Strength = Strength + numberbox
        else:
            val3 = IntVar(value=0)
        
        if spec == 1:
            val4 = IntVar(value=1)
            specialbox = ['!','@','#','#','$','%','^','&','*','(',')']
            Strength = Strength + specialbox
        else:
            val4 = IntVar(value=0)

        global lowercase
        global uppercase
        global number
        global special
        StrengthLabel = Label(settings, text='Strength', fg="Black", font="Arial 12 bold")
        StrengthLabel.pack(padx=10, anchor=NW)
        lowercase = Checkbutton(settings, text = "Lower Case", variable = val1, onvalue = 1, offvalue = 0, height = 1, width = 10)
        uppercase = Checkbutton(settings, text = "Upper Case", variable = val2, onvalue = 1, offvalue = 0, height = 1, width = 10)
        number = Checkbutton(settings, text = "Numbers", variable = val3, onvalue = 1, offvalue = 0, height = 1, width = 8)
        special = Checkbutton(settings, text = "Special Characters", variable = val4, onvalue = 1, offvalue = 0, height = 1, width = 15)
        
        lowercase.pack(anchor=NW) 
        uppercase.pack(anchor=NW) 
        number.pack(anchor=NW) 
        special.pack(anchor=NW)
        
        savedLabel = Label(settings, fg="Green", font=("Arial", 12))
        savedLabel.pack(side = BOTTOM)
        
        savebutton = Button(settings, text='Save', fg='black', font=("Arial", 20), height = 1, width = 10, command=save_settings)
        savebutton.pack(side = BOTTOM)

        settings.protocol("WM_DELETE_WINDOW",settings_on_closing)
        settings.mainloop()
    else:
        print('File does not exist')

def print_value(value):
    return value

def on_closing():
     root.clipboard_clear()
     root.destroy()

def securePass():

    password = ""
    passlen = s.get()
    Strength = []
    while len(password) != passlen:
        f = open(filename,'r+')
        data = json.load(f)
        lower = data['settings']['lowercase']
        upper = data['settings']['uppercase']
        num = data['settings']['numbers']
        spec = data['settings']['special']
        
        if lower == 1:
            lowerbox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            Strength = Strength + lowerbox
        else:
            lowerbox = []

        if upper == 1:
            upperbox = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            Strength = Strength + upperbox
        else:
            upperbox = []

        if num == 1:
            numberbox = ['1','2','3','4','5','6','7','8','9','0']
            Strength = Strength + numberbox
        else:
            numberbox = []

        if spec == 1:
            specialbox = ['!','@','#','#','$','%','^','&','*','(',')']
            Strength = Strength + specialbox
        else:
            specialbox = []

        strength = Strength
        letters = random.choice(strength)
        password = password + letters
    root.clipboard_clear()
    root.clipboard_append(password)
    w.configure(text=password)
    print(password)
    return password

def open_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r+')
    f = open(filename,'r+')
    data = json.load(f)
    data['settings']['data_file'] = fob.name
    f.seek(0)
    f.truncate()
    f.write(json.dumps(data))
    #file = filedialog.askopenfile()
    #print(file.read())

def file_save():
    file = filedialog.asksaveasfilename(filetypes=[("SQLite3 Database File", ".db")], defaultextension=".db")
    fob=open(file,'w')
    fob.write("")
    fob.close()
    def sql_connection():
        try:
            con = sqlite3.connect(fob.name)
            return con
        except Error:
            print(Error)
    def sql_table(con):
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE account_info(account_id integer PRIMARY KEY, email text, password text, name text, url text, created_date text)")
        con.commit()
    con = sql_connection()
    sql_table(con)

root = Tk()
root.configure(background='grey')
sw = int(root.winfo_screenwidth() / 2)
sh = int(root.winfo_screenheight() / 3)
screen_resolution = str(sw)+'x'+str(sh)
print(screen_resolution)
root.title(title)
root.geometry(screen_resolution)
#root.resizable(False,False)#

menubar = Menu(root)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Local Database', command = file_save)
file.add_command(label ='Open Local Database', command = open_file)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Settings', command = settings)
view = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='View', menu = view)
view.add_command(label ='Local Database', command = local_data_screen)
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='About', command = about_screen)
root.config(menu = menubar)


p = securePass

w = Label(root, text="Click Generate to Start",font=("Arial", 30))
w.configure(background="grey")
w.pack(pady=10)

s = Scale(root, length=400,width=15, from_=6, to=30,highlightthickness=0,troughcolor='#73B5FA', tickinterval=24,sliderrelief='flat',activebackground='#1065BF', orient=HORIZONTAL,command=print_value)
s.configure(background='grey')
s.pack(pady=20)

redbutton = Button(root, text='Generate', fg='black', font=("Arial", 20), height = 1, width = 15, command=securePass)
redbutton.pack(pady=10)

warn = Label(root, text="**Generated Password Automatically Copies to Clipboard**", fg="pink", font=("Arial", 9))
warn.configure(background="grey")
warn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
